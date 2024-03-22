'use client'
import { useRouter } from 'next/navigation';
import React, { useState } from 'react';
import styles from '../../css/signin.module.scss';

const Login = () => {
  const [data, setdata] = useState({});
  const [error, setError] = useState('');
  const router = useRouter();

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setdata({ ...data, [name]: value });
  };

  console.log(data)

  const handleLogin = async (e) => {
    e.preventDefault();
    const { email, password } = data;

    if (!email.endsWith('sece.ac.in')) {
      setError('email must end with "sece.ac.in"');
      return;
    }

    if (password.length <= 6) {
      setError('Password must be more than 6 characters');
      return;
    }

    try {
      const response = await fetch('/api/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
      });

      const data1 = await response.json();
      if (data1.status == true) {
        localStorage.setItem('token', data1.access_token);
        router.replace('/dashboard/upcoming');
      } else {
        setError('Login failed. Please check your credentials.');
        setdata({ email: '', password: '' });
      }
    } catch (error) {
      setError('An error occurred while logging in. Please try again later.');
      console.error('Error:', error);
    }
  };

  return (
    <section className="bg-gray-50">
      <div className={styles.signin+" flex flex-col justify-center px-6 py-8 mx-auto md:h-screen lg:py-0 "}>
        
        <div className={styles.loginbox}>
          <div className=" p-6 space-y-4 md:space-y-6 sm:p-8">
            <h1 className="flex justify-center text-6xl font-bold leading-tight tracking-tight text-gray-900">
              Sign In
            </h1>
            <form onSubmit={handleLogin}>
              <div className="space-y-4 md:space-y-6">
                <div>
                  <label htmlFor="email" className="block mb-2 text-sm text-bold font-medium text-gray-900">Your email</label>
                  <input
                    type="text"
                    name="email"
                    id="email"
                    value={data.email}
                    onChange={handleInputChange}
                    className="bg-white border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"
                    placeholder="yourname@sece.ac.in"
                    required
                  />
                </div>
                <div>
                  <label htmlFor="password" className="block mb-2 text-sm font-medium text-gray-900">Password</label>
                  <input
                    type="password"
                    name="password"
                    id="password"
                    value={data.password}
                    onChange={handleInputChange}
                    className="bg-white border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"
                    placeholder="your password"
                    required
                  />
                </div>
                
                {error && <div style={{ color: 'red' }}>{error}</div>}
                <button
                  type="submit"
                  className="w-full text-white bg-blue-600 hover:bg-blue-700 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center"
                >
                  Sign in
                </button>
                
              </div>
            </form>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Login;
