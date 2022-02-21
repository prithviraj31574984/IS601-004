<table><tr><td> <em>Assignment: </em> M4-Simple-Calc</td></tr>
<tr><td> <em>Student: </em> Prithvi Raj Goravi Dattathreya(pg79)</td></tr>
<tr><td> <em>Generated: </em> 2/21/2022 11:30:47 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S22/m4-simple-calc/grade/pg79" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p>Make sure you&#39;re working in an up to date branch</p>
<ul>
<li><code>git checkout dev</code></li>
<li><code>git pull origin dev</code></li>
<li><code>git checkout -b M4-Simple-Calc</code></li>
</ul>
<p>This will likely be started in class.</p>
<p>Steps:</p>
<ol>
<li>Create a new Folder called M4</li>
<li>Create a new file called MyCalc.py inside this folder</li>
<li>Create a MyCalc Class</li>
<li>Define basic addition / subtraction / multiplication / division functions<ol>
<li>These functions should update an internal variable as a running total/value called <code>ans</code></li>
<li>All functions must properly handle the math given standard math scenarios (i.e., show proper messages when trying to divide by zero)</li>
<li>Since you&#39;ll likely be taking screenshots of the code, make sure you add a comment with your ucid and the date</li>
</ol>
</li>
<li>Define a &quot;main&quot; logic to run when the program runs</li>
<li>This logic should ask for user input<ol>
<li>The input can be any valid number, any valid math operator, and any valid number (i.e., 2 * 2)<ol>
<li>This will do an immediate calculation, print it, and store the answer in the <code>ans</code> variable</li>
</ol>
</li>
<li>Alternatively, the input can be <code>ans</code>, any valid math operator, any valid number (i.e., <code>ans</code> * 2)<ol>
<li>This will use the previous answer (or 0 if not set) as part of the calculation, print it, and will store the new answer in the <code>ans</code> variable</li>
</ol>
</li>
</ol>
</li>
<li>Create a test case for each scenario that utilize functions to have expected input and compare against expected output, all cases should pass<ol>
<li>Test number-add-number</li>
<li>Test ans-add-number</li>
<li>Test number-sub-number</li>
<li>Test ans-sum-number</li>
<li>Test number-mult-number</li>
<li>Test ans-mult-number</li>
<li>Test number-div-number</li>
<li>Test ans-div-number</li>
</ol>
</li>
<li>Create a new file called m4_submission.md inside the M4 folder</li>
<li>Fill out the below deliverables</li>
<li>Generate the markdown and paste it into the m4_submission.md</li>
<li><code>git add .</code></li>
<li><code>git commit -m &quot;adding m4 hw&quot;</code></li>
<li><code>git push origin M4-Simple-Calc</code></li>
<li>Create a pull request M4-Simple-Calc to dev</li>
<li>Create a pull request dev to prod (after the previous one is merged)</li>
<li>Navigate to the prod branch on github, go to the M4 folder, click the m4_submission.md</li>
<li>Submit this link to Canvas</li>
</ol>
</td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Snippets (Make sure each screenshot has a comment showing your ucid and the date it was written) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of valid Addition Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/154994580-93c2cc1e-1fe4-447b-ade3-28822154d5ef.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>addition function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of valid Subtraction Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/154994652-47c687c9-f6ed-4ea1-9084-156d6f2c17a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Subtraction Function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of valid Multiplication Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/154994700-354d9f05-9275-42b1-9f2a-2278d33aa6af.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Multiplication Function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of valid division Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/154994752-369d179b-1d0b-42af-866c-c0f4fed215b4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Multiplication Function<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Test Case Validations </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of passing number-add-number Test Case (should test multiple values via fixture)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/154993697-5761528d-eb78-4877-b571-62538e0f8cc7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>addition test case<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of passing ans-add-number Test Case (should test multiple values via fixture, ans should be a cached value from a previous case)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/154993697-5761528d-eb78-4877-b571-62538e0f8cc7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>answer + number test case<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of passing number-sub-number Test Case (should test multiple values via fixture)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/154993909-8b84998e-3dc2-4404-9bc5-ddc2cddde0b7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>subtraction test case<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of passing ans-sub-number Test Case (should test multiple values via fixture, ans should be a cached value from a previous case)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/154993909-8b84998e-3dc2-4404-9bc5-ddc2cddde0b7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>answer -- number test case<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Screenshot of passing number-mult-number Test Case (should test multiple values via fixture)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/154994050-2b1fdaf2-5834-426d-b456-f25da8cf5284.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>multiplication test case<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Screenshot of passing ans-multi-number Test Case (should test multiple values via fixture, ans should be a cached value from a previous case)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/154994050-2b1fdaf2-5834-426d-b456-f25da8cf5284.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>answer * number test case<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Screenshot of passing number-div-number Test Case (should test multiple values via fixture, ans should be a cached value from a previous case)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/154994165-2559956e-cc65-4888-bbb6-523d564ea6f3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>division test case<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 8: </em> Screenshot of passing ans-div-number Test Case (should test multiple values via fixture, ans should be a cached value from a previous case)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/97992883/154994165-2559956e-cc65-4888-bbb6-523d564ea6f3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>answer / number test case<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Briefly talk about anything you learn during this assignment/module</td></tr>
<tr><td> <em>Response:</em> <p>i mainly learned about the python test cases and how the test cases<br>can be automatically checked without any manual testing<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Discuss how test cases work and anything new you learned about them while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <p>test cases check all the operations in a go<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the pull request of M4-Simple-Calc to Dev link</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/prithviraj31574984/IS601-004/pull/6">https://github.com/prithviraj31574984/IS601-004/pull/6</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S22/m4-simple-calc/grade/pg79" target="_blank">Grading</a></td></tr></table>
