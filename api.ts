const API_BASE_URL = "http://127.0.0.1:8000"

export interface User {
  id: number
  username: string
  email: string
}

export interface Case {
  id: number
  title: string
  description: string
  location: string
  crime_type: string
  severity: "Low" | "Medium" | "High"
  date_reported: string
  user_id: number
  created_at?: string
}

export interface LoginCredentials {
  username: string
  password: string
}

export interface RegisterData {
  username: string
  email: string
  password: string
}

export interface CreateCaseData {
  title: string
  description: string
  location: string
  crime_type: string
  severity: "Low" | "Medium" | "High"
  date_reported: string
  user_id: number
}

export interface ApiError {
  detail: string
}

async function handleResponse<T>(response: Response): Promise<T> {
  if (!response.ok) {
    const error: ApiError = await response.json().catch(() => ({ detail: "An error occurred" }))
    throw new Error(error.detail || `HTTP error! status: ${response.status}`)
  }
  return response.json()
}

export async function registerUser(data: RegisterData): Promise<User> {
  const response = await fetch(`${API_BASE_URL}/users`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  })
  return handleResponse<User>(response)
}

export async function loginUser(credentials: LoginCredentials): Promise<User> {
  const response = await fetch(`${API_BASE_URL}/users/login`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(credentials),
  })
  return handleResponse<User>(response)
}

export async function createCase(data: CreateCaseData): Promise<Case> {
  const response = await fetch(`${API_BASE_URL}/cases`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  })
  return handleResponse<Case>(response)
}

export async function getAllCases(): Promise<Case[]> {
  const response = await fetch(`${API_BASE_URL}/cases`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  })
  return handleResponse<Case[]>(response)
}

export async function getCasesByUser(userId: number): Promise<Case[]> {
  const response = await fetch(`${API_BASE_URL}/cases/by-user?user_id=${userId}`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  })
  return handleResponse<Case[]>(response)
}
