import React, { useEffect, useState } from 'react';

const UserList = () => {
  const [users, setUsers] = useState([]);
  const [newUser, setNewUser] = useState({ username: '', email: '', password: '' });

  useEffect(() => {
    fetch('/api/v1/users')
      .then(response => response.json())
      .then(data => {
        if (data.users) {
          setUsers(data.users);
        }
      })
      .catch(error => {
        console.error('Error:', error);
      });
  }, []);

  const handleSubmit = (event) => {
    event.preventDefault();

    // Make a POST request to create a new user
    fetch('/api/v1/users', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(newUser),
    })
      .then(response => response.json())
      .then(data => {
        console.log(data); // Log the response from the API
        setUsers([...users, newUser]); // Add the new user to the list
        setNewUser({ username: '', email: '', password: '' }); // Reset the form fields
      })
      .catch(error => {
        console.error('Error:', error);
      });
  };

  const handleChange = (event) => {
    setNewUser({ ...newUser, [event.target.name]: event.target.value });
  };

  return (
    <div>
      <h1>User List</h1>
      {users.map(user => (
        <div key={user.id}>
          <h3>{user.username}</h3>
          <p>Email: {user.email}</p>
        </div>
      ))}

      <h2>Add User</h2>
      <form onSubmit={handleSubmit}>
        <label htmlFor="username">Username:</label>
        <input
          type="text"
          id="username"
          name="username"
          value={newUser.username}
          onChange={handleChange}
        />

        <label htmlFor="email">Email:</label>
        <input
          type="email"
          id="email"
          name="email"
          value={newUser.email}
          onChange={handleChange}
        />

        <label htmlFor="password">Password:</label>
        <input
          type="password"
          id="password"
          name="password"
          value={newUser.password}
          onChange={handleChange}
        />

        <button type="submit">Add User</button>
      </form>
    </div>
  );
};

export default UserList;
