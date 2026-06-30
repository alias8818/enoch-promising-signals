# N-Gram Draft Speculative Decoding

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `n-gram-draft-speculative-decoding-0acad1cfb114`
Run ID: `n-gram-draft-speculative-decoding-0acad1cfb114-20260522T135735156917+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/579f753113a8

## What looked useful

N-gram copy drafting achieved 0.794 mean target-call reduction on distilgpt2 over 96 generated tokens per case, and 0.719 mean reduction on gpt2-medium over 64 generated tokens per case, with exact greedy equivalence in every case. The larger model showed weakness on low-repeat prose: 0.125 acceptance and 0.406 target-call reduction.

## Boundaries and scale limits

Small synthetic/local prompt regimes only; no production KV-cache verifier, no broad corpus benchmark, no sampling evaluation, and no learned-draft baseline. Wall-clock timings are local proxy measurements from a Python full-context implementation.

## Claim scope

In a local exact-greedy verifier using cached distilgpt2 and gpt2-medium targets, deterministic n-gram copy drafts reduced target forward calls on small repeated/structured/local prompts while preserving token-id identical greedy output.

## Why it stopped

Evidence supports the mechanism locally but is proxy-scale and not a full production serving validation, so it should not be advanced as paper-positive.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should implement a KV-cache verifier and evaluate repeated-code, structured-data, and low-repeat corpora against no-draft greedy plus a learned/speculator baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache n-gram draft speculative decoding on representative corpora
- Success threshold: At least 30% target-call reduction and 15% wall-clock speedup on repeated-code or structured-data corpora, exact greedy equivalence for all evaluated prompts, and a clear regime boundary showing where n-gram drafting is not useful.
- Stop condition: Stop if KV-cache wall-clock speedup is below 5% despite at least 30% target-call reduction, or if representative corpora show under 10% target-call reduction outside synthetic repetition.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-draft-speculative-decoding-0acad1cfb114`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
