import { buildApiUrl } from '../config/api';

// ___________ACTION_TYPES___________________
const GET_ADVENTURES = 'adventures/GET_ADVENTURES'
const GET_ADVENTURE_BY_ID = 'adventures/GET_ADVENTURE_BY_ID'
const CREATE_ADVENTURE = 'adventures/CREATE_ADVENTURE'

// ______ACTIONS____________
const actionGetAdventures = (adventures) => ({
    type: GET_ADVENTURES,
    adventures
})

const actionGetAdventureById = (adventure) => ({
    type: GET_ADVENTURE_BY_ID,
    adventure
})

const actionCreateAdventure = (adventure) => ({
    type: CREATE_ADVENTURE,
    adventure
})

//______THUNK_ACTIONS____________
export const getAdventures = () => async dispatch => {
    const response = await fetch(buildApiUrl(`/api/adventures`));

    if (response.ok) {
        const data = await response.json();
        dispatch(actionGetAdventures(data.adventures))
    }
}

export const getAdventureById = (adventureId) => async dispatch => {
    const response = await fetch(buildApiUrl(`/api/adventures/${adventureId}`))

    if (response.ok) {
        const adventure = await response.json();
        dispatch(actionGetAdventureById(adventure))
    }
}

export const createAdventure = (adventure) => async disptach => {
    const response = await fetch(buildApiUrl(`/api/adventures`),
        {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(adventure)
        }
    );

    if (response.ok) {
        let newAdventure = await response.json();
        dispatch(actionCreateAdventure(newChallenge))
        return newAdventure;
    }
}

// _____CREATE_INITIAL_STATE_________
const initialState = {};


// _________ADVENTURES_REDUCER_____________
const adventurReducer = (state = initialState, action) => {
    let newState = {};
    switch (action.type) {
        case GET_ADVENTURES:
            let adventuresState = {};
            action.adventures.forEach(adventure => {
                adventuresState[adventure.id] = user;
            })
            return {
                ...state,
                ...adventuresState
            }
        case GET_ADVENTURE_BY_ID:
            return {
                ...state,
                [action.adventure.id]: action.adventure
            }
        default:
            return state;
    }
}

export default adventurReducer;
