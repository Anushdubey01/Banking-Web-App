

# Banklance: Your Financial Command Center

---

## Table of Contents

1. [Introduction](#introduction)
2. [Tech Stack](#tech-stack)
3. [Features](#features)
4. [Installation and Setup](#installation-and-setup)
5. [Code Examples](#code-examples)
6. [Resources](#resources)
7. [Further Reading](#further-reading)

---

## Introduction

**Banklance** is a modern, secure platform that simplifies and unifies financial management. Built with **Next.js**, Banklance allows users to connect multiple bank accounts, access real-time transaction data, perform peer-to-peer fund transfers, and gain deep financial insights. This cohesive application integrates advanced financial tools and ensures both convenience and robust security tailored to today’s users.

---

## Tech Stack

- **Frontend**: Next.js, TypeScript, React Hook Form, TailwindCSS
- **Backend**: Appwrite for backend services and authentication
- **Financial Integrations**: Plaid (bank connectivity), Dwolla (fund transfers)
- **Data Validation**: Zod
- **UI Components and Visualization**: ShadCN, Chart.js

---

## Features

- **Secure Authentication**: Server-Side Rendering (SSR) authentication with comprehensive user validation and access control.
- **Multi-Bank Connectivity**: Link multiple bank accounts via Plaid for an all-in-one financial view.
- **Dashboard**: Get an overview of total balances, recent transactions, and categorized spending insights.
- **Account Management**: View, add, or remove connected banks and monitor transaction details.
- **Transaction History**: Access paginated, filterable transaction history across all linked accounts.
- **Real-Time Synchronization**: Automatic updates across the app for recent transactions and account balances.
- **Fund Transfers**: Peer-to-peer transfers via Dwolla, with recipient validation and secure processing.
- **Responsive Design**: Fully optimized for desktop, tablet, and mobile devices for consistent user experience.

---

## Installation and Setup

### Prerequisites

Ensure the following tools are installed:

- [Git](https://git-scm.com/)
- [Node.js](https://nodejs.org/en) and [npm](https://www.npmjs.com/)

### Steps to Set Up Banklance Locally

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Anushdubey01/Banking-Web-App.git
   cd Banking-Web-App
   ```

2. **Install Dependencies**

   ```bash
   npm install
   ```

3. **Configure Environment Variables**

   Set up environment variables by creating a `.env` file in the project root and adding the following keys:

   ```plaintext
   # NEXT.js
   NEXT_PUBLIC_SITE_URL=

   # APPWRITE Configuration
   NEXT_PUBLIC_APPWRITE_ENDPOINT=https://cloud.appwrite.io/v1
   NEXT_PUBLIC_APPWRITE_PROJECT=
   APPWRITE_DATABASE_ID=
   APPWRITE_USER_COLLECTION_ID=
   APPWRITE_BANK_COLLECTION_ID=
   APPWRITE_TRANSACTION_COLLECTION_ID=
   APPWRITE_SECRET=

   # PLAID Configuration
   PLAID_CLIENT_ID=
   PLAID_SECRET=
   PLAID_ENV=
   PLAID_PRODUCTS=
   PLAID_COUNTRY_CODES=

   # DWOLLA Configuration
   DWOLLA_KEY=
   DWOLLA_SECRET=
   DWOLLA_BASE_URL=https://api-sandbox.dwolla.com
   DWOLLA_ENV=sandbox
   ```

4. **Start the Development Server**

   To launch the application locally:

   ```bash
   npm run dev
   ```

   Open [http://localhost:3000](http://localhost:3000) in your browser to view the application.

---

## Code Examples

Here are a few sample snippets to illustrate the core functionality of Banklance.

### Fetch User Balance from Connected Banks

```typescript
import { useEffect, useState } from 'react';

function fetchUserBalance(userId: string) {
    // Fetch balance logic here
}

export default function UserBalance({ userId }) {
    const [balance, setBalance] = useState<number | null>(null);

    useEffect(() => {
        fetchUserBalance(userId).then(setBalance);
    }, [userId]);

    return (
        <div>
            <h3>User Balance</h3>
            <p>{balance !== null ? `$${balance.toFixed(2)}` : "Loading..."}</p>
        </div>
    );
}
```

### Initiate a Fund Transfer

```typescript
import { transferFunds } from './dwollaAPI';

async function initiateTransfer(amount: number, recipientId: string) {
    try {
        const transfer = await transferFunds(amount, recipientId);
        console.log("Transfer Successful:", transfer);
    } catch (error) {
        console.error("Transfer Failed:", error);
    }
}
```

---

## Resources

- [Appwrite Documentation](https://appwrite.io/docs)
- [Plaid API Documentation](https://plaid.com/docs/)
- [Dwolla API Documentation](https://developers.dwolla.com/)
- [Next.js Documentation](https://nextjs.org/docs)

---
