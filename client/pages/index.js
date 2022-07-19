import Head from 'next/head'
import Image from 'next/image'
import { useState, useEffect } from 'react';
import styles from '../styles/Home.module.css'
import { Tab } from '@headlessui/react'

import Category from '../components/category'

export default function Home() {
  const [budgets, setBudgets] = useState([]);
  const [categories, setCategories] = useState([]);

  const newFetch = () => {
    fetch('http://127.0.0.1:8000/budget/170d68d3-5ce0-4083-bc0a-2c55b545f85d')
      .then(response => response.json())
      .then(data => console.log(data))
      .catch(error => {
        console.log('Looks like there was a problem: ', error);
      })
  }

  const fetchPostData = {
    name: 'asdf',
    budget_id: 'f77fcefd-640a-4265-9ad7-915ac71ff7bc'
  }
  const fetchPost = () => {
    fetch('http://localhost:8000/budget/create', {
      method: "PUT",
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      },
      body: JSON.stringify(fetchPostData)
    })
    .then(response => response.json())
    .then(data => console.log(data))
  }

  const updateBudgetName = () => {
    fetch('http://localhost:8000/budget/update', {
      method: "PATCH",
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      },
      body: JSON.stringify({
        id: '170d68d3-5ce0-4083-bc0a-2c55b545f85d',
        name: 'Update from patch'
      })
    })
    .then(response => response.json())
    .then(data => console.log(data))
  }

  const deleteBudget = () => {
    fetch('http://localhost:8000/budget/delete/cb57f494-56be-4898-8d30-9c830a8a81e3', {
      method: "DELETE",
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      }
    })
    .then(response => response.json())
    .then(data => console.log(data))
  }

  const addCategory = () => {
    console.log('add budget');
    let testCat = {
      title: 'Test Budget',
      amount: ''
    }
    setCategories(categories => [...categories, testCat])
  }

  useEffect(() => {
    fetch('http://localhost:8000/budget/get_all', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      },
    })
    .then(response => response.json())
    .then(data => setBudgets(data))
  }, [])

  return (
    <div className={styles.container}>
      <Head>
        <title>Every Budget</title>
        <meta name="description" content="Generated by create next app" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <div className="flex flex-row justify-between">
        <div>
          <h1 className='text-3xl font-bold underline'>Every Budget</h1>
          <a href="/fileupload">File Upload</a>

          <button className="border-2 border-rose-500"
            onClick={newFetch}>
            Test Fetch
          </button>
          <button className="border-2 border-rose-500"
            onClick={fetchPost}>
            Test - POST
          </button>

          <input placeholder={"enter here..."}></input>
          <button className="border-2 border-rose-500"
            onClick={updateBudgetName}>Update</button>

          <label>Delete</label>
          <button className="border-2 border-rose-500"
            onClick={deleteBudget}>Delete</button>
        </div>

        <div>
          <ul>
            {(budgets && budgets.length > 0) ? budgets.map(b => {
              return (
                <li id={b.id}>
                  <div>{b.id}</div>
                  <div>{b.date_created}</div>
                  <div>{b.name}</div>
                </li>
              )
            }) : ''}
          </ul>
        </div>
        
        <Tab.Group defaultIndex={0}>
          <Tab.List>
            <Tab>
              {/* "Home" - Budget */}
                <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                  <path strokeLinecap="round" strokeLinejoin="round" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
                </svg>
            </Tab>
            <Tab>
              {/* Transactions */}
              <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                <path strokeLinecap="round" strokeLinejoin="round" d="M3 10h18M3 14h18m-9-4v8m-7 0h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z" />
              </svg>
            </Tab>
            <Tab>
              {/* Settings */}
              <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                <path d="M5 4a1 1 0 00-2 0v7.268a2 2 0 000 3.464V16a1 1 0 102 0v-1.268a2 2 0 000-3.464V4zM11 4a1 1 0 10-2 0v1.268a2 2 0 000 3.464V16a1 1 0 102 0V8.732a2 2 0 000-3.464V4zM16 3a1 1 0 011 1v7.268a2 2 0 010 3.464V16a1 1 0 11-2 0v-1.268a2 2 0 010-3.464V4a1 1 0 011-1z" />
              </svg>
            </Tab>
          </Tab.List>
          <Tab.Panels>
            <Tab.Panel>
              Budget View

              {/* 
                We can use this Tabs UI element as a "mini-router" for displaying what's on screen.
                - All of the data (except for settings) for this app really needs to be accessible on the same page anyway
              */}
              <main className={styles.main}>
                {categories && categories.length > 0 ? 
                  categories.map((category, idx) => {
                    return (<Category key={idx} />);
                  } ) : 
                  <Category key={0} />}

                <button onClick={addCategory}>Add</button>
              </main>

            </Tab.Panel>
            <Tab.Panel>Transaction View</Tab.Panel>
            <Tab.Panel>Settings</Tab.Panel>
          </Tab.Panels>
        </Tab.Group>
      </div>


      <footer className={styles.footer}>
        <a
          href="https://vercel.com?utm_source=create-next-app&utm_medium=default-template&utm_campaign=create-next-app"
          target="_blank"
          rel="noopener noreferrer">
          Powered by{' '}
          <span className={styles.logo}>
            <Image src="/vercel.svg" alt="Vercel Logo" width={72} height={16} />
          </span>
        </a>
      </footer>
    </div>
  )
}
