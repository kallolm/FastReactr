import React, { useState } from 'react';
import { TextField, Button, Box, Grid, Snackbar } from '@mui/material';
import {BASE_URL} from './conf';

const UserCreationPage = () => {
  const [user, setUser] = useState({
    name: '',
    email: '',
    password: '',
  });

  const [notification, setNotification] = useState({
    open: false,
    message: '',
    severity: 'success',
  });

  const handleChange = (event) => {
    const { name, value } = event.target;
    setUser((prevUser) => ({ ...prevUser, [name]: value }));
  };

  const handleSubmit = () => {
    fetch("/api/users", {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(user),
    })
      .then((response) => response.json())
      .then((data) => {
        setNotification({
          open: true,
          message: JSON.stringify(data),
          severity: 'success',
        });
      })
      .catch((error) => {
        setNotification({
          open: true,
          message: error.message,
          severity: 'error',
        });
      });
  };

  const handleNotificationClose = () => {
    setNotification((prevNotification) => ({
      ...prevNotification,
      open: false,
    }));
  };

  return (
    <Box
      display="flex"
      justifyContent="center"
      alignItems="center"
      height="100vh"
    >
      <Grid container spacing={2} justifyContent="center">
        <Grid item xs={12} sm={6} md={4}>
          <Box p={2} boxShadow={2}>
            <TextField
              label="Name"
              name="name"
              value={user.name}
              onChange={handleChange}
              fullWidth
              margin="normal"
            />
            <TextField
              label="Email"
              name="email"
              value={user.email}
              onChange={handleChange}
              fullWidth
              margin="normal"
            />
            <TextField
              label="Password"
              name="password"
              value={user.password}
              onChange={handleChange}
              fullWidth
              margin="normal"
            />
            <Button variant="contained" onClick={handleSubmit} fullWidth>
              Create User
            </Button>
          </Box>
        </Grid>
      </Grid>
      <Snackbar
        open={notification.open}
        message={notification.message}
        autoHideDuration={3000}
        onClose={handleNotificationClose}
        severity={notification.severity}
      />
    </Box>
  );
};

export default UserCreationPage;
