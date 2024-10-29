<h1 align=center>Portfolio Project 5</h1>

<h2 align=center>Elegant Essentials</h2>

## FINAL DESIGN
![Final project image home page](documentation/PP5_AIR.png) [Am I Responsive](https://amiresponsive.co.uk/)

[Please follow this link to view the final project](https://elegant-essentials-1b55310ae644.herokuapp.com/shop/)

#

## PROJECT IDEA

My idea for this project stems from my PP4, which I developed a spa website for. I wanted to create a B2C e-commerce project based on a similar idea and have decided on an online beauty shop. 
The website offers a selection of products and features, such as buying beauty products, leaving reviews for the shop, signing up to a newsletter service, contacting the shop via a conatct form and more.

When planning the project the most important features to me were:

1. Welcoming homepage
2. Good selection of products
3. User-friendly interface
4. Product descriptions and intersting product images
5. Simple design to allow users to navigate the website easily
6. Search functionality to help users find products easily
7. Contact form for customers
8. Search bar to allow customers to find certain products quickly

#

## UX / UI

## OVERVIEW

- The website was created using Django and features CRUD (Create, Read, Update, Delete) functionality and a user-friendly UI to make buying products from the website sraightforward.
The overall navigation is easy to use and simple to understand so users can find anything they are looking for quickly.
- The user can sign up to the website and when logged in, they can buy products from the shop, leave reviews, as well as edit and delete these.
All other functionalities (e.g. contacting the store and reading reviews from authorised users) are accessible by all site users not matter if they have an account or not.
- Logged-in users can see their past orders and default profile (shipping) information.
The overview of past orders placed has a clickable order number that opens a past order confirmation page, so the user can see where the particular order was shipped to and what phone number was given for the order when it was placed.
- Admin users have extra functionality in the admin panel, being able to search orders by date and username. They can also approve reviews that users have written, so they become visible on the website for everyone to read. Admins can delete orders and user profiles, add questions and answers to the FAQ page and add more products to the website store or delete products if required.
Furthermore, they can view contact requests that might have been sent to the store.

#

### User Stories

To plan the User Stories for this project I have created a Kanban board in Github which can be viewed [here](https://github.com/users/runabrandes/projects/4).

**Agile Methodology** was used throughout the project and "issues" moved on the Kanban board according to what was being worked on at the time. As user stories were accomplished, they were moved in the GitHub Kanban board from **ToDo**, to **In Progress** to **Done**. A row for **Future Implementations** was added as well, which currently holds 3 items, that are not yet implemented, but would be beneficial features the website could have in the future.
**MoSCoW** was also used for this project to help prioritise implementation of features.

#

### Strategy

#### Project Setup

- Django Application: Create the initial Django application tailored for Elegant Essentials.
- File Structure: Organise the project files to ensure maintainability.
- Database Models: Define and establish models to capture relevant data.
- Static Files: Link custom CSS files and images for a polished look.
- Base Template: Create a base.html file for consistent layout across all sites.
- Google Fonts: Integrate Google Fonts for enhanced typography.

#### UX Enhancements
- Favicon: Add a Favicon logo for brand recognition.
- Product Listings in Shop: Display inviting images of products, featuring a  description and their cost.
- Styled Auth Pages: Customise the default allauth pages to reflect the website's overall styling.
- Home Page: Create an inviting homepage showcasing the shop's introduction so customers knwo what the website offers right away.
- Shop Button on Home Page: So users can access the shop immediately and don't have to search for it.
- Order History: Allow users to view past orders and past information.
- User Notifications: Display alerts and messages to inform users about statuses of relevant sections.

#### Navigation
- Navbar: Ensure an easy to use navigation bar across all relevant pages for easy access to different sites.
- Footer: Implement a standard footer on all pages for additional information (privacy policy), newsletter signup link and social media link (Facebook).

#### CRUD
- CRUD was implemented for the reviews section featured in the Elegant Essentials project
- Users that are logged into their existing and verified profile can write reviews. These require to be authorised prior to them being visible to other users. 
- Logged in users can also update and delete their reviews as desired. 
- When a user decides to update their review, authorisation by an admin is required again before the updated review is visible to other users. 

#### Authentication
- User Accounts: Enable users to create and manage their personal account information.
- Allauth Setup: Configure Django Allauth for robust user authentication.

#### Validation
- Form Validation: For all forms across the website to prevent faulty orders being placed. 
- Ensure only the user who placed an order can view their past confirmation. Assign orders to the logged in user profile.

#### Administration
- Admin Search: Allow admins to search and filter orders.
- User Account Management: Let users update their account details.
- Review Authorisation: Equip admins with tools in the admin panel so they can confirm reviews.

#### Deployment
- Amazon Web Services (AWS) for Media and Static.
- PostgreSQL: for Database services. 
- Heroku Deployment: Deploy the application on Heroku.
- DEBUG Settings: Ensure the application is deployed with DEBUG set to False.

#### Testing
- Testing: Conduct thorough testing to ensure a smooth user experience and validate code (HTML and CSS validator, Python Linter, WAVE testing).

#### Documentation
- README: Create comprehensive documentation to guide in navigating and using the application as well as explaining the purpose of the website. 
- Testing: Create comprehensive documentation (TESTING.md) showcasing the different testing approaches. 

#

### Scope

#### Simple and Intuitive UX

- Create a responsive navigation bar for easy access to all pages.
- Develop a footer with social media links and privacy policy and newsletter signup link (button).
- Focus on inviting design for shop products to make users interested in browsing the shop.
- Ensure that users receive visual notifications (alerts or redirects to confirmation pages) for all actions they undertake, such as placing orders, signing up to the newsletter, leaving a review.
- Maintain user orientation throughout their website experience, enhancing usability.
This is achieved by using similar styling and colour schemes throughout the website. 

#### Relevant Content

- Ensure all available products are clearly listed on the site.
- Write informative product descriptions and add clear product images.
- Implement an easy to understad checkout page and checkout process.
- Offer a contact page for users in case they have requests or questions.
- Add a FAQ page with helpful questions and answers so users can find help quickly.
- Allow users to leave reviews so they can share their feedback with other users as well as the site admins so possible issues can be resolved / highlighted.

#### Responsiveness

- Create a responsive website that functions seamlessly across all devices and screen sizes.

#

