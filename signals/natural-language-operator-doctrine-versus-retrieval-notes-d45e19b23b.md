# Natural-language operator doctrine versus retrieval notes with stronger retrieval controls

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `natural-language-operator-doctrine-versus-retrieval-notes-d45e19b23b`
Run ID: `natural-language-operator-doctrine-versus-retrieval-notes-d45e19b23b-20260628T214420684907+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Memory Architecture: Reusable Operator Doctrine vs Retrieval-Only Notes: enoch://control-plane/projects/memory-architecture-reusable-operator-doctrine-vs-retrieval-only-notes-18ffc02f9ef0/runs/memory-architecture-reusable-operator-doctrine-vs-retrieval-only-notes-18ffc02f9ef0-20260628T204420165342+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/387447cd57fb

## What looked useful

Retrieval notes with stronger controls cannot be treated as a drop-in replacement for prompt doctrine across model capacities. Correct retrieval was enough for Qwen2.5-1.5B on this small benchmark, but Qwen2.5-0.5B ignored retrieved policy notes often while following the same rules as prompt doctrine.

## Boundaries and scale limits

Synthetic multiple-choice tasks only; hand-constructed retrieval bundles; no live tool execution, production retrieval, randomized large benchmark, frontier model, or 7B+ validation.

## Claim scope

On an 8-case synthetic operator-choice benchmark, prompt doctrine was reliable for both tested Qwen2.5 instruct models; retrieved notes were reliable for Qwen2.5-1.5B when the relevant note was present, but failed frequently for Qwen2.5-0.5B even under filtered retrieval controls.

## Why it stopped

Bounded synthetic evidence is mixed and not publication-grade; it supports a mechanism-level caution but not a broad validation or rejection.

## Recommended next action

Stop this run as no-paper useful signal; next bounded deepen test should use a randomized 50+ case benchmark with live retrieval, note-order randomization, adversarial distractors, and at least one stronger open model.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Randomized live-retrieval operator doctrine versus retrieval-note benchmark
- Success threshold: Prompt doctrine or controlled retrieval must show at least a 15 percentage point accuracy or false-allow improvement over weak retrieval, with retrieval recall and parse rate reported.
- Stop condition: Stop if all conditions remain within 5 percentage points across models or if live retrieval recall is too low to isolate instruction-use behavior.

## Evidence references

- Artifact root: `<local-path>/projects/natural-language-operator-doctrine-versus-retrieval-notes-d45e19b23b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
