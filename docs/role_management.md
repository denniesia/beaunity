### 🔒 Role Management

Beaunity is designed with public and private areas to balance community engagement with controlled interactions.

#### Public Area (Accessible to Everyone)
🔧 Anonymous users can only view public content—events, challenges, posts, and categories—on the landing page. 
They cannot interact, comment, or manage any content.

#### Private Area (Requires Account & Roles)

🔧 User – Regular members with full interaction abilities: they can join/leave events and challenges, like/unlike, add to favourites, comment, and manage their own comments and profiles.

🔧 Organizer – Focused on event creation, able to add, edit, and delete their own events.

🔧 Moderator – Handles content moderation in the private space, approving posts/challenges and managing categories.

🔧 Superuser – Full administrative rights, including changing user group memberships and accessing all areas.

| Groups          | Event                                                                                                                                                                                                     | Challenge                                                                                                                                                                                                                                                                                                               | Post                                                                                                                                                                      | Category                                                                                     | Accounts                                                      |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| Anonymous User | Can only view the events on the landing page.                                                                                                                                                             | Can only view the challenges on the landing page.                                                                                                                                                                                                                                                                       | Can view posts                                                                                                                                                            | Can view categories                                                                          | -                                                             | 
| User           | Can view events<br/>Can join/leave events<br/>Can like/unlike events<br/>Can add events to Favourites<br/>Can comment on events<br/>Can edit own comments on events<br/>Can delete own comments on events | Can view challenges<br/>Can add challenges<br/>Can edit own challenges<br/>Can delete own challenges<br/>Can join/leave challenges<br/>Can like/unlike challenges<br/>Can add challenges to Favourites <br/>Can comment on challenges<br/>Can edit own comments on challenges<br/>Can delete own comments on challenges | Can view posts<br/>Can like/unlike posts<br/>Can add posts to Favourites<br/>Can comment on posts<br/>Can edit own comments on posts<br/>Can delete own comments on posts | Can view categories                                                                          | Can view profiles<br/>Can edit profile<br/>Can delete profile |
| Organizer      | Can view events<br/>Can add events<br/>Can edit own events<br/>Can delete own events                                                                                                                      | -                                                                                                                                                                                                                                                                                                                       | -                                                                                                                                                                         | -                                                                                            | -                                                             |
| Moderator      | -                                                                                                                                                                                                         | Can approve challenges<br/>Can post challenges without approval                                                                                                                                                                                                                                                         | Can approve posts<br/>Can post posts without approval                                                                                                                     | Can add categories<br/>Can view categories<br/>Can edit categories<br/>Can delete categories | -                                                             |
| Superuser      | All of the above                                                                                                                                                                                          | All of the above                                                                                                                                                                                                                                                                                                        | All of the above                                                                                                                                                          | All of the above                                                                             | Can change group belonging                                    |


This separation ensures that public visitors can explore safely, while registered users and staff interact and manage 
content in a controlled, community-driven environment.

#### 🔫 Key Components

- If anonymous users attempt to access restricted content, they will be redirected to the login page.
- If authenticated users attempt to access content they do not have permission to view, they will be denied access and 
a custom *403 Forbidded* template will appear.

<img width="1368" height="943" alt="image" src="https://github.com/user-attachments/assets/812ba005-21ca-4d9e-93a2-66ee6a049a91" />


- If users attempt to access content that does not exist, a custom *404 Page not Found* template will appear.

<img width="1328" height="943" alt="image" src="https://github.com/user-attachments/assets/deeffd23-1567-4abf-906d-e7912deff66a" />


- Staff members see an extra "Administration" option in the navigation.
 
<img width="1534" height="90" alt="image" src="https://github.com/user-attachments/assets/7324ec03-7106-4359-acc0-f570a641f95f" />


- Options in the "Administration" dropdown menu vary based on the user’s group. *Organizers* can access only My Events options, whereas *Superusers* and *Moderators* have full access.  

<img width="1420" height="208" alt="image" src="https://github.com/user-attachments/assets/1a53eb20-d5be-4579-b00d-18fcde2794ee" />

- The section *My Events* provides quick overview of the user's own events, with sorting options available for better organization.

<img width="1346" height="952" alt="image" src="https://github.com/user-attachments/assets/cef7927b-f0e3-494f-bd57-05d72f1a90f1" />


- The *Categories* section provides an overview of the Categories, including title and description. The categories can be edited and deleted only by members with such permissions.

<img width="1175" height="946" alt="image" src="https://github.com/user-attachments/assets/40195cc8-c48d-4f6a-bc88-cc1d0d1962cf" />

Edit category view: 

<img width="1239" height="946" alt="image" src="https://github.com/user-attachments/assets/305fd784-f5d5-40bc-985f-29f2a08e884a" />

Create category view:
<img width="1239" height="937" alt="image" src="https://github.com/user-attachments/assets/2137486e-f583-4ec9-914d-55ab31584f6f" />


- The *Challenges* section provides an overview of Pending Challenges, displaying their titles and details. Using the action icons, challenge can easily be approves or rejected. Approving a challenge automatically send its author email with approval confirmation. 

<img width="1249" height="946" alt="image" src="https://github.com/user-attachments/assets/65839bd4-cf47-475b-aa9d-c72f1ff704a1" />



- The *Posts* section provides an overview of Pending Posts, displaying their titles and content. Using the action icons, challenge can easily be approves, rejected or edited. Approving a post automatically send its author email with approval confirmation. 
 
  <img width="1341" height="942" alt="image" src="https://github.com/user-attachments/assets/672281f5-7e40-40f1-bf03-ea7d56edcd96" />

Edit post view: Staff members can only edit the category of the post, the other fields are readonly.

<img width="1415" height="948" alt="image" src="https://github.com/user-attachments/assets/eb4a1fed-4f5a-4db1-8f7c-db9da0cecf60" />


- 💊 Superuser can view and change the group belonging of the users.
<img width="1341" height="944" alt="image" src="https://github.com/user-attachments/assets/2c32f645-8855-41b7-a35f-5f6681d12ae2" />

<img width="1370" height="948" alt="image" src="https://github.com/user-attachments/assets/37dff23c-cbe9-4733-9fdb-284db16f35bd" />

🐛  Error Handling

Event Create Page

<img width="1402" height="944" alt="image" src="https://github.com/user-attachments/assets/c218d4c8-c53d-4e92-973b-d18b00e44f9b" />


