import React, { useState } from "react";
import signupimage from "../../images/signup-g.svg";
import { Link } from "react-router-dom";
import ScrollToTop from "../ScrollToTop";
import {registerUser} from "../../api/Api";

const MyAccountSignUp = () => {


    const [formData, setFormData] = useState({
      firstname: "",
      lastname: "",
      email: "",
      password: "",
    });
  
    const handleChange = (e) => {
      setFormData({ ...formData, [e.target.name]: e.target.value });
    };
  
    const handleSubmit = async (event) => {
      event.preventDefault();
  
      const userData = {
        firstname: formData.firstname,
        lastname: formData.lastname,
        email: formData.email,
        password: formData.password,
      };
      // console.log("=1=1=1=1=1=1=1=1=1==1=1=1===1===1=1=", userData) ok
  
      try {
        const response = await registerUser(userData);
        alert(response.message); 
      } catch (error) {
        alert(error.response?.data?.detail || "Registration failed");
      }
    };

  return (
    <div>
      <>
        <ScrollToTop />
      </>
      <>
        {/* section */}
        <section className="my-lg-14 my-8">
          {/* container */}
          <div className="container">
            {/* row */}
            <div className="row justify-content-center align-items-center">
              <div className="col-12 col-md-6 col-lg-4 order-lg-1 order-2">
                {/* img */}
                <img src={signupimage} alt="freshcart" className="img-fluid" />
              </div>
              {/* col */}
              <div className="col-12 col-md-6 offset-lg-1 col-lg-4 order-lg-2 order-1">
                <div className="mb-lg-9 mb-5">
                  <h1 className="mb-1 h2 fw-bold">Get Start Shopping</h1>
                  <p>Welcome to FreshCart! Enter your email to get started.</p>
                </div>
                {/* form */}
                <form action="POST" onSubmit={handleSubmit}>
                  <div className="row g-3">
                    {/* col */}
                    <div className="col">
                      {/* input */}
                      <input
                        type="text"
                        className="form-control"
                        placeholder="First name"
                        aria-label="First name"
                        alue={formData.firstname}
                        onChange={handleChange}
                        name="firstname"
                        required
                      />
                    </div>
                    <div className="col">
                      {/* input */}
                      <input
                        type="text"
                        className="form-control"
                        placeholder="Last name"
                        aria-label="Last name"
                        name="lastname"
                        value={formData.lastname}
                        onChange={handleChange}
                        required
                      />
                    </div>
                    <div className="col-12">
                      {/* input */}
                      <input
                        type="email"
                        className="form-control"
                        id="inputEmail4"
                        placeholder="Email"
                        name="email"
                        onChange={handleChange}
                        required
                      />
                    </div>
                    <div className="col-12">
                      {/* input */}
                      <input
                        type="password"
                        className="form-control"
                        id="inputPassword4"
                        placeholder="Password"
                        name="password"
                        onChange={handleChange}
                        required
                      />
                    </div>
                    {/* btn */}
                    <div className="col-12 d-grid">
                      {" "}
                      <button type="submit" className="btn btn-primary">
                        Register
                      </button>
                      <span className="navbar-text">
                        Already have an account?{" "}
                        <Link to="/MyAccountSignIn">Sign in</Link>
                      </span>
                    </div>
                    {/* text */}
                    <p>
                      <small>
                        By continuing, you agree to our{" "}
                        <Link to="#!"> Terms of Service</Link> &amp;{" "}
                        <Link to="#!">Privacy Policy</Link>
                      </small>
                    </p>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </section>
      </>
    </div>
  );
};

export default MyAccountSignUp;
