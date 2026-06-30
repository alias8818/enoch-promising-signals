# Speculative Decoding with Suffix-Tree Draft vs. Tiny Neural Draft

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `speculative-decoding-with-suffix-tree-draft-vs-tiny-neural-draft-16ab03b553be`
Run ID: `speculative-decoding-with-suffix-tree-draft-vs-tiny-neural-draft-16ab03b553be-20260620T211355828519+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f2b1df03f253

## What looked useful

Suffix retrieval is a strong first baseline for repetitive workloads because it can recover multi-token continuations cheaply; a tiny neural draft must substantially exceed suffix acceptance to overcome proposal overhead. Low-recurrence stochastic streams showed little speculative gain for either draft.

## Boundaries and scale limits

No real transformer target model, tokenizer, target probability acceptance, KV-cache behavior, batching, or GPU serving loop was tested. Corpora were synthetic and the tiny neural draft was a small GRU trained locally for up to 25 epochs.

## Claim scope

On bounded synthetic token-stream probes with gamma=4, a suffix-table draft produced higher or comparable speculative acceptance than a tiny GRU draft, especially on exact/noisy recurrence and deterministic counter-like regimes, while both methods were ineffective on stochastic Markov-like data.

## Why it stopped

Stopped as a no-paper useful signal: the result is a synthetic/proxy mechanism test, not full validation of LLM speculative decoding speedup.

## Recommended next action

Run a small real-transformer speculative decoding harness comparing suffix retrieval and a parameter-matched tiny neural draft on recurrence-stratified prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-transformer recurrence-stratified suffix draft vs tiny neural draft
- Success threshold: Suffix retrieval is useful if it achieves at least 90% of the tiny neural draft's accepted tokens per verifier call at less than 25% of draft overhead on high-recurrence prompts, with no claimed win on low-recurrence prompts unless measured speedup exceeds 1.15x.
- Stop condition: Stop if both drafts emit fewer than 1.15 tokens per verifier call or end-to-end speedup is below 1.05x on high-recurrence prompts after overhead is included.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-decoding-with-suffix-tree-draft-vs-tiny-neural-draft-16ab03b553be`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
