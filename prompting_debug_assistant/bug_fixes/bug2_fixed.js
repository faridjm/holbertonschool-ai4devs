function calculateDiscount(price, percent) {
    const discount = price * percent / 100;
    return price - discount;
}

function main() {
    const price = 100;
    const percent = 20;
    const finalPrice = calculateDiscount(price, percent);
    console.log(`Final price: ${finalPrice}`);
}

main();
