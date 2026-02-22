from pydantic import BaseModel


class SignupRequest(BaseModel):
    email: str
    password: str
    confirm_password: str


class LoginRequest(BaseModel):
    email: str
    password: str
    

class RefreshTokenRequest(BaseModel):
    refresh_token: str
    

class OTPVerificationRequest(BaseModel):
    otp: str


class ForgotPasswordRequest(BaseModel):
    email: str


class ResetPasswordRequest(BaseModel):
    password: str
    confirm_password: str