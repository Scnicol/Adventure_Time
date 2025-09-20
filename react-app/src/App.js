import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Switch } from "react-router-dom";
import SignupFormPage from "./components/SignupFormPage";
import LoginFormPage from "./components/LoginFormPage";
import { authenticate } from "./store/session";
import Navigation from "./components/Navigation";
import HomePage from "./components/HomePage";
import MyAdventuresPage from "./components/MyAdventuresPage/MyAdventuresPage";
import AdventureDetailPage from "./components/AdventureDetailPage";
import ActivitiesPage from "./components/ActivitiesPage/ActivitiesPage";
import FoodPage from "./components/FoodPage/FoodPage";
import { buildApiUrl } from "./config/api";

function App() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);
  useEffect(() => {
    fetch(buildApiUrl("/api/csrf/restore"), { credentials: "include" });
    dispatch(authenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);

  return (
    <>
      <Navigation isLoaded={isLoaded} />
      {isLoaded && (
        <Switch>
          <Route exact path="/">
            <HomePage />
          </Route>
          <Route path="/my-adventures">
            <MyAdventuresPage />
          </Route>
          <Route path="/login" >
            <LoginFormPage />
          </Route>
          <Route path="/signup">
            <SignupFormPage />
          </Route>
          <Route path="/adventures/:adventureId">
            <AdventureDetailPage />
          </Route>
          <Route path="/activities">
            <ActivitiesPage />
          </Route>
          <Route path="/food">
            <FoodPage />
          </Route>
        </Switch>
      )}
    </>
  );
}

export default App;
