# Deploy Environment Checklist (Session/Cookie/CORS)

- SESSION_COOKIE_SAMESITE = "None"
- SESSION_COOKIE_SECURE = True
- CSRF_COOKIE_SAMESITE = "None"
- CSRF_COOKIE_SECURE = True
- CORS_ALLOW_CREDENTIALS = True
- CORS_ALLOWED_ORIGINS 에 프론트엔드 배포 주소(https://airbnb-frontend-u9m8.onrender.com) 포함

이 설정이 모두 적용되어야 프론트엔드와 백엔드가 다른 도메인일 때 인증이 정상 동작합니다.
