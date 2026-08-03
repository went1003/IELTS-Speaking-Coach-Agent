# Local Data Plan

This project keeps private learning data separate from public coaching rules.

```text
data/
├── raw_documents/       # Read-only personal sources and transcripts
├── working_documents/   # Editable derivatives
├── database/            # Future SQLite learning records
└── output/              # Generated private reports
```

These four directories are excluded from GitHub through `.gitignore`.

Do not copy personal documents into the public repository merely to make the first version appear complete. Version 0.1 can be validated with non-sensitive sample text or with files that remain local.

## Vocabulary

| English | 中文 | Meaning in this project |
|---|---|---|
| Raw document | 原始资料 | A supplied source that the system must not overwrite |
| Working document | 工作文档 | An editable derivative of a raw source |
| Learning record | 学习记录 | Structured history that should survive after the program closes |
| Session report | 单次训练报告 | Feedback generated after one practice session |
| Source label | 来源标签 | A tag that distinguishes real, adapted, model, and unverified material |
