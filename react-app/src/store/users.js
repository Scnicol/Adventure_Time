// ______ACTION_TYPES____________
const GET_USERS = 'users/GET_USERS'
const GET_USER_BY_ID = 'users/GET_USER_BY_ID'


// ______ACTIONS_______________
const actionGetUsers = (users) => ({
    type: GET_USERS,
    users
})

const actionGetUserById = (user) => ({
    type: GET_USER_BY_ID,
    user
})

// _______THUNK_ACTIONS_________
export const getUsers = () => async dispatch => {
    const response = await fetch(`/api/users`);

    if (response.ok) {
        const data = await response.json();
        dispatch(actionGetUsers(data.users))
    }
}

export const getUserById = (userId) => async dispatch => {
    const response = await fetch(`/api/users/${userId}`)

    if (response.ok) {
        const user = await response.json();
        dispatch(actionGetUserById(user))
    }
}

// _____CREATE_INITIAL_STATE_________
const initialState = {};

// _________USERS_REDUCER_____________
const userReducer = (state = initialState, action) => {
    let newState = {};

    switch (action.type) {
        case GET_USERS:
            let usersState = {};
            action.users.forEach(user => {
                usersState[user.id] = user;
            })
            return {
                ...state,
                ...usersState
            }
        case GET_USER_BY_ID:
            return {
                ...state,
                [action.user.id]: action.user}
        default:
            return state;
    }
}

export default userReducer;
