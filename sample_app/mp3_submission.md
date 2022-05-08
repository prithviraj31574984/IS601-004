<table><tr><td> <em>Assignment: </em> Mini Project 3 - Flask AdvCalc</td></tr>
<tr><td> <em>Student: </em> Prithvi Raj Goravi Dattathreya(pg79)</td></tr>
<tr><td> <em>Generated: </em> 5/8/2022 12:58:57 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S22/mini-project-3---flask-advcalc/grade/pg79" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol>
<li>Create a new branch called MP3-Flask-AdvCalc</li>
<li>Add the ability to load a basic csv file of mixed sets of data/equations for add/sub/div/mult</li>
<li>Add UI support for your 5 stats functions from MP2 (buttons on the screen that trigger the equation) The user should be able to enter data and run each of your stats functions as expected</li>
<li>Add the ability to load an advanced csv file of fixed data/equations for the 5 stats functions (or load in 5 different files separately)</li>
<li>Give the ability for the user to delete a single history item of theirs</li>
<li>Give the ability for the user to delete all of their history (this should not affect any other user&#39;s history)</li>
<li>Add test cases to <ol>
<li>Register a user</li>
<li>Login the user</li>
<li>To run a calc function for the user and record/create a SimpleHistory (verify this gets created with proper data)</li>
<li>Make sure the User and SimpleHistory data get deleted after the test phase</li>
</ol>
</li>
<li>Fill in the below deliverables (make sure screenshots load properly)</li>
<li>Create an mp3_submission.md file in your project/app folder</li>
<li>Paste the generated markdown into this file</li>
<li>git add/commit/push to MP3-Flask-AdvCalc</li>
<li>Merge to dev</li>
<li>Merge dev to prod</li>
<li>Find the mp3_submission.md in the prod branch on github</li>
<li>Submit the direct link to that file to Canvas</li>
</ol>
</td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Basic CSV Loading </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the mixed csv data of add/sub/mult/div</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/167305626-ce3ae945-a05c-4e9d-b156-2328c4183534.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the mixed data of add/sub/mult/div, square , square root<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the history after uploading the csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/167305674-9628de43-50b3-4fe2-9f65-48a6bf6d62ae.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>history after uploading the csv file<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how the csv is processed and the data is sent to the calculator</td></tr>
<tr><td> <em>Response:</em> <p>The only library needed to work with CSV files is the “csv” Python<br>library. After importing the library and setting the path of our CSV file,<br>we use the “open()” method to begin reading the file line by line.<br>The parsing of the CSV file is handled by the “csv. reader()” method<br>which is discussed in detail later.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Adv Calc Functions </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the new Advanced buttons on the UI</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/167305696-cac9f4e5-e6b3-4344-ad1a-92ed651d534f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the new Advanced buttons on the UI which are sample mean,<br>median, mode ,standard deviation <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the aggregated history of each 5 advanced function being ran</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/167305862-369d876e-f7de-421b-a0a2-d0cbc52eb730.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the aggregated history of standard deviation, median and mean<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/167305894-ec01a6fa-61f7-4773-a496-2c7e84ef4de3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the aggregated history of variance and mode<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain how you updated the calculator to handle the advanced function interaction</td></tr>
<tr><td> <em>Response:</em> <p>by using built in functions, when the user clicks on the button the<br>corresponding if block is chosen and corresponding function is being processes <br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Advanced CSV Loading </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of mixed advanced csv data (or separate csv files if you wish)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/167306256-6dc8d167-3896-4ede-90b4-b807c8e6a342.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of mixed advanced csv data <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the aggregated history the csv file execution</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/167305958-772cd58b-40ac-43bd-a4a3-cba9c70ef69b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the aggregated history the csv file execution<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain how you updated the calculator to handle the advanced function interaction</td></tr>
<tr><td> <em>Response:</em> <p>if block contains the corresponding functions and the corresponding functions are processed<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> History Management </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show a before and after screenshot of deleting a single history item</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/167306312-fa4bcd12-b11f-4a12-9b2f-f720fa96f239.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>before screenshot of deleting a single history item<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/167306378-9f7ebe84-2451-4b58-ae05-e603ff7b0ab5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>after screenshot of deleting a single history item<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Show a before and after screenshot showing the history being cleared (all of it for this user)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/167306312-fa4bcd12-b11f-4a12-9b2f-f720fa96f239.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> before  screenshot showing the history being cleared for the user with<br>user id=3<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Show that the history is still present for other users (that task 2 didn't delete it for other users)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/167306470-18e50ade-aa4d-41a8-b015-11f7c3742362.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>after screenshot showing the history being cleared for the user with user id=3<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain how you implemented single delete of the history</td></tr>
<tr><td> <em>Response:</em> <p>using query which will be proceed<br>DELETE FROM is601_simplehistory<br>WHERE id= &amp; user_id=8;<br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Explain how you implemented deleting all of the logged in user's history</td></tr>
<tr><td> <em>Response:</em> <p>DELETE FROM is601_simplehistory<br>WHERE user_id=8;<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Test Cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot the test case code to register a test user via pytest</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/167306507-7edd8c34-be93-49b2-84e3-2f7d844cda73.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>user successfully registered <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot the passing test case from pytest for task 1</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/167306544-cf083a9c-d5b9-4e99-9fa8-3462855eeb08.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>same user is able to login<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot the test case code for logging in the test user via pytest</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/167306544-cf083a9c-d5b9-4e99-9fa8-3462855eeb08.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>user is able to login<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot the passing test case from pytest for task 3</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/167306615-15380419-18f9-4fea-a3bc-7ba37b80c7c2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>calc home screen<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Screenshot the test case code for recording a SimpleHistory for the test user (should be a valid generation from the calculator)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/167306588-20240476-499b-427e-b156-b6a9c1aaa126.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>simple history of the user <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Screenshot the passing test case from pytest for task 5</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/167306667-7ef45c07-6583-4959-ba6f-980ae5b5901c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>csv upload successful <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain the flow/process of these new test cases that pass the test user around</td></tr>
<tr><td> <em>Response:</em> <p>manual testing<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add a link to your deployed app </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add the link here to the hosted instance</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-004-347913-73bcalrfaa-uc.a.run.app/register">https://is601-004-347913-73bcalrfaa-uc.a.run.app/register</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S22/mini-project-3---flask-advcalc/grade/pg79" target="_blank">Grading</a></td></tr></table>
