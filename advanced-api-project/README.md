# Advanced API Project

## Overview

This project provides an API to manage books using Django REST Framework. The API includes endpoints to list, create, retrieve, update, and delete book instances. Permissions are enforced to allow authenticated users to modify data, while unauthenticated users have read-only access.

## Endpoints

- **GET /api/books/**: Retrieve a list of all books.
- **POST /api/books/**: Create a new book (authenticated users only).
- **GET /api/books/<id>/**: Retrieve details of a specific book.
- **PUT /api/books/<id>/**: Update a specific book (authenticated users only).
- **DELETE /api/books/<id>/**: Delete a specific book (authenticated users only).

## Custom Behavior

- **Validation**: During update, the publication year is validated to ensure it is not in the future.
- **Permissions**: Read-only access for unauthenticated users; authenticated users can create, update, and delete books.

