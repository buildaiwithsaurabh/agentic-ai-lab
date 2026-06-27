import { useEffect, useState } from "react";
import axios from "axios";
import "./index.css";

function App() {

  const [products, setProducts] = useState([]);
  const [productName, setProductName] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadProducts();
  }, []);

  async function loadProducts() {
    try {

      const response = await axios.get(
        "https://fakestoreapi.com/products"
      );

      setProducts(response.data);

    } catch (error) {
      console.log(error);

    } finally {
      setLoading(false);
    }
  }

  function addProduct() {

    if (!productName.trim()) return;

    const newProduct = {
      id: crypto.randomUUID(),
      title: productName
    };

    setProducts([newProduct, ...products]);

    setProductName("");
  }

  function deleteProduct(id) {

    const updatedProducts =
      products.filter(
        product => product.id !== id
      );

    setProducts(updatedProducts);
  }

  if (loading) {
    return <h2>Loading...</h2>;
  }

  return (

    <div className="container">

      <h1>Product Management Dashboard</h1>

      <div className="form">

        <input
          type="text"
          placeholder="Product Name"
          value={productName}
          onChange={(e)=>
            setProductName(e.target.value)
          }
        />

        <button onClick={addProduct}>
          Add Product
        </button>

      </div>

      <div className="grid">

        {
          products.map(product=>(
            <div
              className="card"
              key={product.id}
            >

              <h3>
                {product.title}
              </h3>

              <button
                className="delete"
                onClick={()=>
                  deleteProduct(product.id)
                }
              >
                Delete
              </button>

            </div>
          ))
        }

      </div>

    </div>

  );

}

export default App;