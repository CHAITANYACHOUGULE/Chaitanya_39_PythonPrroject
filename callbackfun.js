function1 = (callback1, callback2, callback3) => {
  setTimeout(() => {
    console.log("function 1 callback succesfully");
    callback1(callback2, callback3);
  }, 1500);
}

function2 = (callback1, callback2) => {
  setTimeout(() => {
    console.log("function 2 callback succesfully");
    callback1(callback2);
  }, 1500);
}

function3 = (callback1) => {
  setTimeout(() => {
    console.log("function 3 callback succesfully")
    callback1()
  }, 1500);
}

function4 = () => {
  setTimeout(() => {
    console.log("function 4 callback succesfully")
  }, 1500);
}

function1(function2, function3, function4);