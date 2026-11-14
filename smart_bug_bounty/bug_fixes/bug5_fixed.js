function sortDeliveryTimes(deliveryTimes) {
  return [...deliveryTimes].sort((a, b) => a - b);
}

const deliveryTimes = [12, 3, 25, 8];
const sortedTimes = sortDeliveryTimes(deliveryTimes);

console.log(JSON.stringify({
  sortedTimes,
  originalTimes: deliveryTimes
}));
