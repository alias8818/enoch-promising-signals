# Speculative Cascade: Small Drafts, Selective Large Verification

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `speculative-cascade-small-drafts-selective-large-verification-1fca277d690d`
Run ID: `speculative-cascade-small-drafts-selective-large-verification-1fca277d690d-20260614T051550625734+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/353f49aa9e91

## What looked useful

Confidence gating is diagnostically useful on fixed reference contexts: threshold 0.20 would verify 40.49% of positions and reach 88.997% token agreement if rejected tokens followed the verifier trajectory. In the actual autoregressive cascade, accepted draft tokens changed future contexts; threshold 0.30 reached only 54.88% token agreement and 12.50% exact sequence match at 41.41% verifier calls, while threshold 0.70 still reached only 72.92% token agreement and 35.94% sequence match at 72.59% verifier calls.

## Boundaries and scale limits

This run used small GPT-2-family models, greedy decoding, single-prompt inference, short continuations, and no KV-cache serving benchmark. It does not validate larger models, production latency, block speculative decoding, human preference, or downstream task quality.

## Claim scope

On a bounded 64-prompt, 24-token greedy decoding test with distilgpt2 drafts and gpt2 verification, small-model confidence predicts same-context agreement, but a naive one-token autoregressive selective verifier requires high verifier call rates and still has low sequence fidelity.

## Why it stopped

Bounded direct evidence shows the naive selective verifier is undermined by autoregressive drift; this is a useful early falsification of the simple mechanism, not a full-scale validation.

## Recommended next action

Stop this naive one-token cascade as no-paper evidence; next bounded test should add state-correcting block verification or forced periodic large-model rollback on the same prompt set.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: State-correcting block verification for small-draft cascades
- Success threshold: At least 90% token agreement and at least 50% exact sequence match with gpt2 greedy reference while keeping verifier-call rate at or below 50% on 64 prompts by 24 tokens.
- Stop condition: Stop if block correction cannot exceed 80% token agreement below 60% verifier-call rate or if it requires near-always-large verification to preserve context.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-cascade-small-drafts-selective-large-verification-1fca277d690d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
