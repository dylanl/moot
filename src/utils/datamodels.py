from typing import Optional
from datetime import datetime
from dataclasses import dataclass, field


@dataclass
class User:
    id: int
    username: str
    avatar_hash: Optional[str]
    bio: Optional[str]
    banned: bool
    flags: int


@dataclass
class Moot:
    id: int
    author_id: int
    content: str
    reference: Optional[int]
    hide: bool
    flags: int


@dataclass
class Session:
    token: str
    author_id: int
    expires: datetime


@dataclass
class AuthState:
    user: User = field(default=None)
    session: Session = field(default=None)
