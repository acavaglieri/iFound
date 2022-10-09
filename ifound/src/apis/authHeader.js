import jwt_decode from "jwt-decode";

export function authHeader() {
    try {
        let token = localStorage.getItem('access_token');
        let decode = jwt_decode(token)
        if (token && !(Date.now() >= decode.exp * 1000)) {
            return { headers: { 'Authorization': 'Bearer ' + token } }
        } else {
            logout()
        }
    } catch {
        logout()
    }
}

function logout() {
    localStorage.clear()
    localStorage.setItem('authenticated',false)
    location.reload()
}