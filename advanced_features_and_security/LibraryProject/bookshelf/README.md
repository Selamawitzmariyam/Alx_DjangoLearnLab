# Custom Permissions and Groups Setup

## Step 1: Custom Permissions
- Added `can_view`, `can_create`, `can_edit`, and `can_delete` permissions to the `Article` model.

## Step 2: Groups and Permissions
- Created groups: **Editors**, **Viewers**, and **Admins**.
- Assigned permissions:
  - **Viewers:** can view journals.
  - **Editors:** can view, create, and edit journals.
  - **Admins:** can view, create, edit, and delete journals.

## Step 3: Enforcing Permissions
- Used `@permission_required` decorators in views to restrict access.

## Step 4: Testing
- Created test users and assigned them to groups.
- Verified permissions by attempting different actions.
