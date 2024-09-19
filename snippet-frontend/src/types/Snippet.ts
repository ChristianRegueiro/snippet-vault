import type { Tag } from './Tag'

export interface Snippet {
    id: number
    tags: Tag[],
    created_at: string
    updated_at: string
    name: string
    description: string
    code: string
    language: string
    pinned: boolean
}