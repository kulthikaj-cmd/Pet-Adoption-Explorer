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



## 10. Application Architecture
The project will use a modular structure based on a three-layer architecture.
Presentation Layer
Responsible for:
- User Interface
- Navigation
- Forms
- Displaying results
Business Logic Layer
Responsible for:
- Search processing
- Input validation
- Filtering logic
- Favorites logic
Data Layer
Responsible for:
- Sample pet data
- Future API integration
- Data access
## 11. Team Members & Roles

| Member | Role | Main Responsibilities |
|---|---|---|
| Donus | Planner / UI Designer | Sprint planning, requirements, UI design, navigation, and documentation |
| Pheem | Developer / Backend | Application structure, search, filtering, pet data, business logic, and API integration |
| Fah | Frontend / Debugger | User interface, pet cards, pet details, favorites, testing, debugging, and bug fixing |

### โดนัส — Planner / UI Designer

- Define Sprint goals and scope
- Define functional requirements
- Design the application layout
- Design navigation and user flow
- Prepare project documentation
- Coordinate team tasks

### ภีม — Developer / Backend

- Develop the application structure
- Prepare sample pet data
- Implement search functionality
- Implement filtering logic
- Develop business logic
- Prepare API integration for future sprints

### ฟ่า — Frontend / Debugger

- Develop the user interface
- Create pet cards
- Create Pet Details page
- Create Favorites interface
- Test application features
- Debug application errors
- Test invalid inputs and edge cases
- Find and fix bugs
12. Development Tasks
1. Create GitHub repository
2. Create project structure
3. Prepare Sprint 1 documentation
4. Create Home page
5. Create navigation
6. Create Explore Pets page
7. Create sample pet dataset
8. Create pet cards
9. Implement search
10. Implement input validation
11. Create Pet Details
12. Create Favorites interface
13. Test application
14. Fix errors
15. Review Sprint 1 requirements
13. Testing Plan
Test Case	Input	Expected Result
Normal search	dog	Dog results are displayed
Uppercase	DOG	Search works correctly
Mixed case	DoG	Search works correctly
Spaces	dog	Spaces are removed
Empty input	""	Validation message is displayed
Spaces only	"   "	Validation message is displayed
No result	elephant	No-result message is displayed


14. Definition of Done
Sprint 1 will be considered complete when:
- GitHub repository is available
- Sprint 1 documentation is completed
- Application can start successfully
- Home page is available
- Navigation works
- Explore Pets page is available
- Sample pet data is available
- Search works
- Input validation works
- Pet cards are displayed
- Basic pet details can be viewed
- Favorites interface is available
- Application does not crash during normal use
- Project structure is ready for Sprint 2
15. Expected Sprint 1 Result
At the end of Sprint 1, the project should have a functional Web Application foundation.
Users should be able to open the application, navigate between the main sections, browse sample pets, search for pets, view basic pet information, and use the favorites interface.
The application structure should be ready for Petfinder API integration and additional features in later sprints.
16. Future Development
Sprint 2
- Petfinder API integration
- Real pet data
- Advanced search
- Filtering
- Pet details
- Improved favorites
- Error and loading states
Sprint 3
- Advanced UI/UX
- Persistent favorites
- Advanced filtering
- Testing
- Performance improvements
- Deployment preparation
Final Application
- Complete Web Application
- Petfinder API
- Search and filtering
- Pet details
- Favorites
- Responsive UI
- Deployment
