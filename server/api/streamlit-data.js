const express = require('express');
const router = express.Router();
const { PrismaClient } = require('@prisma/client');

const prisma = new PrismaClient();

// Helper function to handle errors
const handleError = (res, error) => {
  console.error('API Error:', error);
  return res.status(500).json({ error: 'Internal server error' });
};

// Get property statistics
router.get('/properties/stats', async (req, res) => {
  try {
    const propertyCount = await prisma.property.count();
    const propertyTypes = await prisma.property.groupBy({
      by: ['type'],
      _count: { id: true }
    });
    const propertyStatus = await prisma.property.groupBy({
      by: ['status'],
      _count: { id: true }
    });

    return res.json({
      totalProperties: propertyCount,
      byType: propertyTypes,
      byStatus: propertyStatus
    });
  } catch (error) {
    return handleError(res, error);
  }
});

// Get property list with details
router.get('/properties', async (req, res) => {
  try {
    const properties = await prisma.property.findMany({
      include: {
        owner: {
          select: {
            id: true,
            username: true,
            firstName: true,
            lastName: true
          }
        },
        facilities: {
          select: {
            id: true,
            name: true,
            type: true,
            isAvailable: true
          }
        }
      }
    });
    return res.json(properties);
  } catch (error) {
    return handleError(res, error);
  }
});

// Get tenant statistics
router.get('/tenants/stats', async (req, res) => {
  try {
    const tenantCount = await prisma.tenant.count();
    const tenantsPerProperty = await prisma.tenant.groupBy({
      by: ['facilityId'],
      _count: { id: true }
    });

    return res.json({
      totalTenants: tenantCount,
      byFacility: tenantsPerProperty
    });
  } catch (error) {
    return handleError(res, error);
  }
});

// Get financial data
router.get('/financial', async (req, res) => {
  try {
    const startDate = req.query.startDate ? new Date(req.query.startDate) : new Date(new Date().getFullYear(), 0, 1);
    const endDate = req.query.endDate ? new Date(req.query.endDate) : new Date();

    const payments = await prisma.payment.findMany({
      where: {
        paymentDate: {
          gte: startDate,
          lte: endDate
        }
      },
      orderBy: {
        paymentDate: 'asc'
      }
    });

    const expenses = await prisma.expense.findMany({
      where: {
        expenseDate: {
          gte: startDate,
          lte: endDate
        }
      },
      orderBy: {
        expenseDate: 'asc'
      }
    });

    return res.json({
      payments,
      expenses
    });
  } catch (error) {
    return handleError(res, error);
  }
});

// Get maintenance tasks
router.get('/maintenance', async (req, res) => {
  try {
    const tasks = await prisma.task.findMany({
      where: {
        category: 'MAINTENANCE'
      },
      include: {
        property: {
          select: {
            id: true,
            name: true
          }
        },
        facility: {
          select: {
            id: true,
            name: true
          }
        },
        assignedTo: {
          select: {
            id: true,
            username: true,
            firstName: true,
            lastName: true
          }
        }
      }
    });

    const tasksByStatus = await prisma.task.groupBy({
      by: ['status'],
      where: {
        category: 'MAINTENANCE'
      },
      _count: { id: true }
    });

    return res.json({
      tasks,
      byStatus: tasksByStatus
    });
  } catch (error) {
    return handleError(res, error);
  }
});

// Get occupancy data
router.get('/occupancy', async (req, res) => {
  try {
    const facilities = await prisma.facility.count();
    const occupiedFacilities = await prisma.facility.count({
      where: {
        isAvailable: false
      }
    });

    const tenants = await prisma.tenant.findMany({
      include: {
        facility: true
      }
    });

    // Calculate occupancy rate
    const occupancyRate = facilities > 0 ? occupiedFacilities / facilities : 0;

    return res.json({
      totalFacilities: facilities,
      occupiedFacilities,
      occupancyRate,
      tenants
    });
  } catch (error) {
    return handleError(res, error);
  }
});

module.exports = router;