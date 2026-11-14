function findProductById(products, id) {
  for (const product of products) {
    if (product.id === id) {
      return product;
    }
  }

  return null;
}

const products = [
  { id: 101, name: "Notebook" },
  { id: 102, name: "Pencil" },
  { id: 103, name: "Ruler" }
];

console.log(findProductById(products, 102));
