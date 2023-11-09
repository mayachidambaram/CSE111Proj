SELECT u_firstname AS FirstName, u_lastname AS LastName, u_email AS Email, u_phonenum AS PhoneNumber
FROM User
WHERE u_firstname = 'John' AND u_lastname = 'Doe';
-- Displays name and contact info of a specific user
