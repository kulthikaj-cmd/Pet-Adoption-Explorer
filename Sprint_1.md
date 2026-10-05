# Pet Adoption Explorer — Sprint 1 Report

## 1. Sprint Overview

**Project:** Pet Adoption Explorer  
**Course:** CP352301 Script Programming  
**Sprint:** Sprint 1 — Application Foundation  
**Project Type:** Web Application

---

## 2. Sprint Goal

The goal of Sprint 1 is to establish the foundation of the Pet Adoption Explorer Web Application.

The sprint focuses on creating the initial user interface, navigation, pet exploration, search functionality, input validation, and a modular project structure.

A local sample dataset will be used during Sprint 1. Petfinder API integration will be developed in a later sprint.

---

## 3. Project Objective

Pet Adoption Explorer is a web application designed to help users discover pets that are available for adoption.

Users will be able to explore pets, search for pets, view pet information, and save pets that they are interested in.

The final application is planned to integrate real pet data through the Petfinder API.

---

## 4. Sprint 1 Scope

### 4.1 In Scope

- Web Application foundation
- Home Dashboard
- Sidebar Navigation
- Explore Pets page
- Pet search
- Pet cards
- Basic pet information
- Basic pet details
- Favorites interface
- Local sample pet dataset
- Input validation
- Modular project structure
- Basic error handling

### 4.2 Out of Scope

- Petfinder API integration
- Real-time pet data
- User authentication
- Database
- Advanced filtering
- Deployment
- Advanced recommendation system
- AI features

---

## 5. Functional Requirements

### FR-01: Application Start

The application must start successfully and display the main application interface.

### FR-02: Home Dashboard

The Home page must display a welcome message and provide access to the main application features.

### FR-03: Navigation

Users must be able to navigate between the main sections using the navigation menu.

### FR-04: Explore Pets

Users must be able to view available pets from the local sample dataset.

### FR-05: Search Pets

Users must be able to enter a search term to find pets.

### FR-06: Input Validation

The system must:

- Remove unnecessary spaces using `.strip()`
- Convert text to lowercase using `.lower()`
- Prevent empty search input
- Handle invalid input without crashing

### FR-07: Pet Details

Users should be able to view basic information about a selected pet.

### FR-08: Favorites

Users should be able to select a pet as a favorite.

---

## 6. Application Flow

User  
↓  
Home Dashboard  
↓  
Navigation  
↓  
Explore Pets  
↓  
Search / Browse Pets  
↓  
Select Pet  
↓  
View Pet Details  
↓  
Add to Favorites  
↓  
Favorites

---

## 7. User Interface

### 7.1 Home Page

The Home page will contain:

- Application name
- Welcome message
- Search bar
- Browse by pet type
- Featured pets
- Navigation to Explore Pets

### 7.2 Explore Pets

The Explore Pets page will contain:

- Search field
- Pet type selection
- Pet cards
- Pet name
- Breed
- Age
- Gender
- Location
- Details button

### 7.3 Pet Details

The Pet Details page will display:

- Pet image
- Pet name
- Animal type
- Breed
- Age
- Gender
- Location
- Description
- Favorite button

### 7.4 Favorites

The Favorites page will display pets selected by the user.

---

## 8. Sample Dataset

Sprint 1 will use a local sample dataset instead of real API data.

Each pet record should contain:

- ID
- Name
- Type
- Breed
- Age
- Gender
- Location
- Description
- Image

---

## 9. Input Validation

Search input will be normalized before processing.

Example:

```python
search_text = search_text.strip().lower()
