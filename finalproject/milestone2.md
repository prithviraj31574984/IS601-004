<table><tr><td> <em>Assignment: </em> IS601 Milestone 2 Shop Project</td></tr>
<tr><td> <em>Student: </em> Prithvi Raj Goravi Dattathreya(pg79)</td></tr>
<tr><td> <em>Generated: </em> 5/11/2022 2:27:49 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S22/is601-milestone-2-shop-project/grade/pg79" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol>
<li>Checkout Milestone2 branch </li>
<li>Create a new markdown file called milestone2.md</li>
<li>git add/commit/push immediate</li>
<li>Fill in the below deliverables</li>
<li>At the end copy the markdown and paste it into milestone2.md</li>
<li>Add/commit/push the changes to Milestone2</li>
<li>PR Milestone2 to dev and verify</li>
<li>PR dev to prod and verify</li>
<li>Checkout dev locally and pull changes to get ready for Milestone 3</li>
<li>Submit the direct link to this new milestone2.md file from your GitHub prod branch to Canvas</li>
</ol>
<p>Note: Ensure all images appear properly on github and everywhere else.
Images are only accepted from Google Cloud, not localhost.
All website links must be from Google Cloud. </p>
</td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Users with admin or shop owner will be able to add products </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of admin create item page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/167763752-4af55b38-f1e7-4e0f-ab5b-107dbd077020.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Admin Dashboard where he can add products, see order history and update the<br>products<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/167764862-37f5e0ea-825f-45c0-867f-019b6c70a73c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>product being displayed in admin_dashboard <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot of populated Products table clearly showing the columns</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/167872073-6bab9a61-59b7-4323-bfc4-55ba00132239.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Database Screenshot of the Products table <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly describe the code flow for creating a Product</td></tr>
<tr><td> <em>Response:</em> <p>Initially system checks whether user role is admin or not. User with admin<br>role can add products from admin_Dahsboard .<br>Admin/Shop Owner can add details like name,<br>description ,category, stock availability, image and price of a product.<br>Also can change visibility<br>of product in product list<br>If the user role Is not admin, our code<br>will not allow that user to go to the admin section, it will<br>redirect user to the login section with error message that please login as<br>admin to access admin page,<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/prithviraj31574984/IS601-004/pull/17">https://github.com/prithviraj31574984/IS601-004/pull/17</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to the related file from Google Cloud</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://online-shop-webapp.herokuapp.com/admin_dashboard">https://online-shop-webapp.herokuapp.com/admin_dashboard</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Any user can see visible products on the Shop Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the Shop page showing 10 items without filters/sorting applied</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/167764438-50fb1790-7c0d-43de-97dd-2c1b50bca3b5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Product being displayed without any filter being displayed <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Shop page showing both filters and a different sorting applied (should be more than 1 sample product)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/167764660-9820a8ce-3f5e-40d3-85a9-05c3cdc1ff24.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>after applying filter only caps are being displayed <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/167764757-13cbd571-afdb-4a7b-8f1a-7ffe6c1ab258.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>after applying filter only Dresses  are being displayed <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the filter/sort logic from the code (ensure ucid and date is shown)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/167765232-04de69d7-e28e-4e13-a4c7-f5fb6cf0dbf2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>sort logic from source code <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Briefly explain how the results are shown and how the filters are applied</td></tr>
<tr><td> <em>Response:</em> <p>System irrespective of user roles, by default display’s  products to all. Filter’s<br>with various categories helps user navigate website better. User can make use of<br>filters to browse relevant items they look for.<br>Those products which have visibility equals<br>True will be shown in the products list and user will see all<br>these products,<br>The query I have used will filter the product table with visibility<br>equals True, all products will be filtered from the products table whose visibility<br>equals true.<br><br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/prithviraj31574984/IS601-004/pull/17">https://github.com/prithviraj31574984/IS601-004/pull/17</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Add a direct link to the related file from Google Cloud</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://online-shop-webapp.herokuapp.com/pro_cat/1">https://online-shop-webapp.herokuapp.com/pro_cat/1</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Show Admin/Shop Owner Product List (this is not the Shop page and should show visibility status) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of the Admin List page/results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/167764862-37f5e0ea-825f-45c0-867f-019b6c70a73c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>product list from admin dash board only admin can access it !!<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain how the results are shown</td></tr>
<tr><td> <em>Response:</em> <p>System checks user role, If user role is admin it displays product list<br>along with details.<br>Admin/Shop Owner can delete products and update product details.<br>User with admin<br>role has a separate admin dashboard, where user with admin role can see<br>all the products which he added to the products table along with all<br>information which only a user with admin role can see, from there user<br>can update the products.<br><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/prithviraj31574984/IS601-004/pull/17">https://github.com/prithviraj31574984/IS601-004/pull/17</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to the related file from Google Cloud</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://online-shop-webapp.herokuapp.com/admin_dashboard">https://online-shop-webapp.herokuapp.com/admin_dashboard</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Admin/Shop Owner Edit button </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a sceenshot showing the edit button visible to the Admin on the Shop page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/167765630-86664ce0-42cb-4b27-943a-da79fcb97379.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit button visible to the Admin only shop page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/167765817-44753203-ead3-4cef-a8a6-1a2ddec27db5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit button not visible to the user only on shop page ( screenshot<br>1 VS Screenshot 2 difference between admin and user on shop page) <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a sceenshot showing the edit button visible to the Admin on the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/167766165-5bc168c1-2672-4c88-923a-bc2c04a2ba8c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit button visible to the Admin on the Product <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/167766312-918dcf0d-70c8-433f-a0ec-5906393b857e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>update page on visible to admin<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a sceenshot showing the edit button visible to the Admin on the Admin Product List Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/167766538-e57ca53a-c8ae-48e9-a188-a72c8cd51993.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> edit button visible to the Admin on the Admin Product List Page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/167766705-9b5f04e4-a5fa-4953-9edd-3537fc211add.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> edit button visible to the Admin on the Admin Product List Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after screenshot of Editing a Product via the Admin Edit Product Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/167766705-9b5f04e4-a5fa-4953-9edd-3537fc211add.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>before  Editing a Product via the Admin Edit Product Page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/167766818-f6f14ab8-4c60-4e4e-96a6-25583f13b38a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>after Editing a Product via the Admin Edit Product Page (the yellow dresss<br>has been deleted)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <p>Admin/shop Owner will be able to see the edit button every where in<br>the products page and home page, our code will only display the edit<br>button when the user have admin role and the product belong to the<br>same admin as the product have.<br>Admin/Shop Owner can edit product profile and if<br>necessary, can modify profile. <br>Admin/Shop Owner can update name, description, category, stock availability,<br>image and price of a product.<br><br></p><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/prithviraj31574984/IS601-004/pull/17">https://github.com/prithviraj31574984/IS601-004/pull/17</a> </td></tr>
<tr><td> <em>Sub-Task 7: </em> Add a direct link to the related file from Google Cloud</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://online-shop-webapp.herokuapp.com/admin_dashboard">https://online-shop-webapp.herokuapp.com/admin_dashboard</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Product Details Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the button (clickable item) that directs the user to the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/167767053-d916d81f-e456-4161-b000-d71e003476cb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The details button will direct us to product detail page!<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the result of the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/167767158-cda0bf05-cdfe-4aef-9303-6d7d94683ed0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Product Details Page with ratings!<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <p>The working of product details page is like if some one click on<br>single product that will take that user to the product details page along<br>with that product id, and in the  the product page our query<br>will filter result with this id and display information about the clicked product.<br><br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/prithviraj31574984/IS601-004/pull/17">https://github.com/prithviraj31574984/IS601-004/pull/17</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to the related file from Google Cloud (can be any specific item)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://online-shop-webapp.herokuapp.com/details/2">https://online-shop-webapp.herokuapp.com/details/2</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add to Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the success message of adding to cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/167767313-73a2d276-de36-4661-83c6-ae7463b5ef81.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> cart screenshot!<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the error message of adding to cart (i.e., when not logged in)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/167767384-12d4beb1-36f1-48b0-888b-647b7784bee1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the error message of adding to cart when not logged in<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Cart table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/167767313-73a2d276-de36-4661-83c6-ae7463b5ef81.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> screenshot of the Cart table with products in it<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Tell how your cart works (1 cart per user; multiple carts per user)</td></tr>
<tr><td> <em>Response:</em> <p>User can select product and add to cart. Users can review or delete<br>items from their cart before making purchase. User can increase or decrease number<br>of items .System checks availability of product and ensure user cannot increase quantity<br>than stock availability.<br>If some one click on add to cart button, with that<br>click our code will receive that product id, with this id code will<br>filter product table and will fetched the specified product and then code will<br>add that product to session and then from session code will display all<br>the info to cart html page</p><br><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Explain the process of add to cart</td></tr>
<tr><td> <em>Response:</em> <p> When a user adds a product to their cart, they may not<br>buy it right away, or at all. So users can review or delete<br>items from their cart.<br>Session object is used to keep shopping cart data.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/prithviraj31574984/IS601-004/pull/17">https://github.com/prithviraj31574984/IS601-004/pull/17</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> User will be able to see their Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the Cart View (show subtotal, total, and the link to Product Details Page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/167767539-ff483b87-8a13-40a2-9260-365e73ce553b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>cart picture <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain how the cart is being shown from a code perspective along with the subtotal and total calculations</td></tr>
<tr><td> <em>Response:</em> <p>Once some one click on add to cart page, it will take the<br>id of the product, then we will use that id to fetch data<br>of that id and pass all the data to session variable and then<br>all the data goes to cart html page, if user add multiple item<br>then our code will loop through cart and fetch price of each product<br>and sum it and show the total result.<br>the total amount of the products,<br>even after the alterations is automatically calculated in order to help the users<br>shop according to their budgets. So user no longer have to manually add<br>the prices of the products to check the total billing amount.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/prithviraj31574984/IS601-004/pull/17">https://github.com/prithviraj31574984/IS601-004/pull/17</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to the related file from Google Cloud</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://online-shop-webapp.herokuapp.com/show_cart">https://online-shop-webapp.herokuapp.com/show_cart</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> User can update cart quantity </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show a before and after screenshot of Cart Quantity update</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/167767539-ff483b87-8a13-40a2-9260-365e73ce553b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> before updating the  Cart Quantity  to one<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/167767690-3aac26a8-4d85-4243-b770-429dac5715a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>after updating the  Cart Quantity   to two<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Show a before and after screenshot of setting Cart Quantity to 0</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/167767690-3aac26a8-4d85-4243-b770-429dac5715a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>before updating   the  Cart Quantity   to zero<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/167767732-091dbf36-af20-4810-ade9-be5a0ce80703.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>after updating the  Cart Quantity   to zero<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Show how a negative quantity is handled</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/167767732-091dbf36-af20-4810-ade9-be5a0ce80703.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cart Quantity   to zero<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain the update process including how a value of 0 and negatives are handled</td></tr>
<tr><td> <em>Response:</em> <p>Value of 0 and negative is handle with if statements, i have put<br>some query function which will send updated value of the item to back<br>end and then that backend data is compared with actual stock of the<br>product, if it’s going out of stock the code will automatically restrict user<br>from adding more value then actual stock.<br>User can increase or remove quantity of<br>item if they need. System checks availability of product and ensure user cannot<br>increase quantity of item than stock availability. Once quantity is increased corresponding price<br>changes will be reflected. Session object is updated. After purchase of product, stock<br>availability count is reduced. <br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/prithviraj31574984/IS601-004/pull/17">https://github.com/prithviraj31574984/IS601-004/pull/17</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Cart Item Removal </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a before and after screenshot of deleting a single item from the Cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/167767948-91520068-6649-4364-b036-a060217c3ab4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>before deleting items in cart as u can see their are two items<br>in the cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after screenshot of clearing the cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/167768053-9f2b39ef-eb07-4e2f-844e-f4c8f13b808b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>after deleting items in cart as u can see their are only one<br>item in the cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how each delete process works</td></tr>
<tr><td> <em>Response:</em> <p>If some one click on delete button associated with each item, it will<br>take id of that product to delete route and it will delete <br>that record from that session.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <em>Response:</em> <p><a href="https://github.com/prithviraj31574984/IS601-004/pull/17">https://github.com/prithviraj31574984/IS601-004/pull/17</a><br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S22/is601-milestone-2-shop-project/grade/pg79" target="_blank">Grading</a></td></tr></table>
