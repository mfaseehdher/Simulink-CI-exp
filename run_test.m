model="add_two_numbers";
out= sim(model);
y=out.simout.Data(end);
expected=5;
assert(y==expected," Test failed, expected 5, got %g",y);
disp(" Test passed");