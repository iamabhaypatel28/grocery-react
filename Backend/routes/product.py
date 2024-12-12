from fastapi import APIRouter, HTTPException, Depends
from schemas.product import ProductRequest, ProductResponse
from config.database import get_db
from sqlalchemy.orm import Session
from models.product import Product

router = APIRouter()



@router.post("/add-product", response_model=ProductResponse)
async def add_product(product: ProductRequest, db: Session = Depends(get_db)):
    
    existing_product = db.query(Product).filter(Product.name == product.name).first()
    if existing_product:
        raise HTTPException(status_code=400, detail="product is already existing.")
    new_product = Product(
        name=product.name,
        price=product.price,
        details=product.datels,
        quantity=product.quantity
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    
    return ProductResponse(message="Product added successfully" , product_id = new_product.id)

@router.get("/get-product")
async def get_product(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    return products

@router.get("/get-product/{id}")
async def get_product(id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found.")
    return product

@router.put("/update-product/{id}")
async def update_product(id: int, product: ProductRequest, db: Session = Depends(get_db)):
    existing_product = db.query(Product).filter(Product.id == id).first()
    if existing_product is None:
        raise HTTPException(status_code=404, detail="Product not found.")
    existing_product.name = product.name
    existing_product.price = product.price
    existing_product.details = product.datels
    existing_product.quantity = product.quantity
    db.commit()
    return {"message": "Product updated successfully."}

@router.delete("/delete-product/{id}")
async def delete_product(id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found.")
    db.delete(product)
    db.commit()
    return {"message": "Product deleted successfully."}