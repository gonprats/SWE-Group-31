const express = require('express');
const authController = require('../controllers/auth');

const router = express.Router();

//submits the form, coming from /auth and posts... final /auth/register
router.post('/register', authController.register)

module.exports = router;