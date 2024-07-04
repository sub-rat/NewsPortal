# Installation
## Create React App
```bash
npx create-react-app news-app
cd news-app
npm start
```

## Dependencies 
```bash
npm install --save react-router-dom bootstrap axios react-bootstrap
```

# Development
## Update index.js for bootstrap support
`./index.js`

```js
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import 'bootstrap/dist/css/bootstrap.min.css';
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

reportWebVitals();
```

## Create Api Service
`./src/apiService.js`

```js
import axios from 'axios';

const apiClient = axios.create({
    baseURL: 'http://localhost:8000', // Replace with your API base URL
    headers: {
        'Content-Type': 'application/json',
    },
});

export const getNews = async () => {
    try {
        const response = await apiClient.get('/api/news');
        return response.data;
    } catch (error) {
        console.error('Error fetching data:', error);
        throw error;
    }
};

export const getNewsDetail = async (id) => {
    try {
        const response = await apiClient.get('/api/news/'+id);
        return response.data;
    } catch (error) {
        console.error('Error fetching data:', error);
        throw error;
    }
};



export const getCategories = async () => {
    try {
        const response = await apiClient.get('/api/categories');
        return response.data;
    } catch (error) {
        console.error('Error fetching data:', error);
        throw error;
    }
};
```

# Create NewsList Page
`.src/components/NewsList.js`

```js
import React, { useEffect, useState } from 'react';
import { getNews } from '../apiService';
import { Card, Container, Row, Col, Spinner, Alert, Button } from 'react-bootstrap';
import { Link } from 'react-router-dom';

const NewsList = () => {
    const [news, setNews] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchNews = async () => {
            try {
                const news = await getNews();
                setNews(news.results);
            } catch (error) {
                setError(error);
            } finally {
                setLoading(false);
            }
        };

        fetchNews();
    }, []);

    if (loading) {
        return <Spinner animation="border" />;
    }

    if (error) {
        return <Alert variant="danger">Error: {error.message}</Alert>;
    }

    return (
        <Container>
            <Row>
                <h1>News</h1>
            </Row>
            <Row>
                {news.map((article) => (
                    <Col key={article.id} md={4} className="mb-4">
                        <Link to={`/detail/${article.id}`} style={{ textDecoration: 'none', color: 'inherit' }}>
                        <Card>
                            <Card.Img variant="top" src={article.image_url} />
                            <Card.Body>
                                <Card.Title>{article.title}</Card.Title>
                            </Card.Body>
                        </Card>
                        </Link>
                    </Col>
                ))}
            </Row>
        </Container>
    );
};

export default NewsList;
```

## Update App.js for Router and Navbar
`.src/App.js`

```js
import React from 'react';
import NewsList from './components/NewsList';
import { Route, BrowserRouter, Routes, Link } from "react-router-dom";
import { Navbar, Nav, Container } from 'react-bootstrap';
import NewsDetail from './components/NewsDetail';

function App() {
    return (
      <BrowserRouter >
       <Navbar bg="dark" variant="dark" expand="lg">
                <Container>
                    <Navbar.Brand as={Link} to="/">NewsApp</Navbar.Brand>
                    <Navbar.Toggle aria-controls="basic-navbar-nav" />
                    <Navbar.Collapse id="basic-navbar-nav">
                        <Nav className="me-auto">
                            <Nav.Link as={Link} to="/">Home</Nav.Link>
                        </Nav>
                    </Navbar.Collapse>
                </Container>
            </Navbar>
        <div className="App">
        <Container className="mt-4">
          <Routes>  
            <Route path="/" element={<NewsList/>} />
            <Route path="/detail/:id" element={<NewsDetail/>} />
          </Routes>
          </Container>
        </div>
      </BrowserRouter >
    );
}

export default App;
```

## Add Detail Page
`./src/components/NewsDetail.js`

```js
// src/components/NewsDetail.js
import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { getNewsDetail } from '../apiService';
import { Container, Spinner, Alert,Row, Col  } from 'react-bootstrap';

const NewsDetail = () => {
    const { id } = useParams();
    const [news, setNews] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchNews = async () => {
            try {
                const news = await getNewsDetail(id);
                setNews(news);
            } catch (error) {
                setError(error);
            } finally {
                setLoading(false);
            }
        };

        fetchNews();
    }, [id]);

    if (loading) {
        return <Spinner animation="border" />;
    }

    if (error) {
        return <Alert variant="danger">Error: {error.message}</Alert>;
    }

    if (!news) {
        return <Alert variant="warning">News not found</Alert>;
    }

    return (
        <Container>
        <Row className="justify-content-center">
            <Col md={8} className="text-center">
                <h2 className="mb-4">{news.title}</h2>
                <img src={news.image_url} alt={news.title} className="img-fluid mb-4" />
                <p className="text-justify">{news.content}</p>
            </Col>
        </Row>
    </Container>
    );
};

export default NewsDetail;


```


