import React, { Component, useState } from "react";
import RecipeChoices from "./RecipeChoices";

import drinksJson from "./drinks.json";

const BaristaForm = () => {
    const [inputs, setInputs] = useState({
        'temperature': '',
        'milk': '',
        'syrup': '',
        'blended': ''
    })

    const ingredients = {
        'temperature': ['hot', 'lukewarm', 'cold'],
        'syrup': ['mocha', 'vanilla', 'toffee', 'maple', 'caramel', 'other', 'none'],
        'milk': ['cow', 'oat', 'goat', 'almond', 'none'],
        'blended': ['yes', 'no', 'turbo']
    }


    let randomDrinkIndex = Math.floor(Math.random() * drinksJson.drinks.length);
    
    const [CurrentDrink, setCurrentDrink] = useState(drinksJson.drinks[randomDrinkIndex].name)
    const [TrueRecipe, setTrueRecipe] = useState(drinksJson.drinks[randomDrinkIndex].ingredients)
    const getNextDrink = () => {
            let randomDrinkIndex = Math.floor(Math.random() * drinksJson.drinks.length);

            //set state variables for current drink and true recipe
            setCurrentDrink(drinksJson.drinks[randomDrinkIndex].name);
            setTrueRecipe(drinksJson.drinks[randomDrinkIndex].ingredients);
    }

    const onNewDrink = () => {
            //set ingredients state as empty
            setInputs({
                'temperature' : '',
                'milk' : '',
                'syrup' : '',
                'blended' : ''
        });

            //call getNextDrink()
            getNextDrink();

    }


    const onCheckAnswer = () => {

    }


    return (
        <div>
            <h2>Hi Id like to order a</h2>
            <form>
                <h3>Temperature</h3>

                <div className="answer-space">
                    {inputs['temperature']}
                </div>
                <RecipeChoices
                    handleChange={(e) => setInputs((prevState) => ({
                        ...prevState,
                        [e.target.name]: e.target.value
                    }))}
                    labels="temperature"
                    choices={ingredients["temperature"]}
                    checked={inputs["temperature"]}
                />

                <h3>Syrup</h3>

                <div className="answer-space">
                    {inputs['syrup']}
                </div>
                <RecipeChoices
                    handleChange={(e) => setInputs((prevState) => ({
                        ...prevState,
                        [e.target.name]: e.target.value
                    }))}
                    labels="syrup"
                    choices={ingredients["syrup"]}
                    checked={inputs["syrup"]}
                />
                

                <h3>Milk</h3>
                <div className="answer-space">
                    {inputs['milk']}
                </div>
                <RecipeChoices
                    handleChange={(e) => setInputs((prevState) => ({
                        ...prevState,
                        [e.target.name]: e.target.value
                    }))}
                    labels="milk"
                    choices={ingredients["milk"]}
                    checked={inputs["milk"]}
                />
                
                <h3>Blended</h3>
                
                <div className="answer-space">
                    {inputs['blended']}
                </div>
                <RecipeChoices
                    handleChange={(e) => setInputs((prevState) => ({
                        ...prevState,
                        [e.target.name]: e.target.value
                    }))}
                    labels="blended"
                    choices={ingredients["blended"]}
                    checked={inputs["blended"]}
                />

            </form>
            <button className="button submit" type="submit" onClick={onCheckAnswer}>
                Check Answer
            </button>
            <button className="button submit" type="new-drink-button" onClick={onNewDrink}>
                New Drink
            </button>

        </div>

    )
}

export default BaristaForm;