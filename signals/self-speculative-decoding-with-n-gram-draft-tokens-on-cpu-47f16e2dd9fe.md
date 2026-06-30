# Self-Speculative Decoding with N-gram Draft Tokens on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `self-speculative-decoding-with-n-gram-draft-tokens-on-cpu-47f16e2dd9fe`
Run ID: `self-speculative-decoding-with-n-gram-draft-tokens-on-cpu-47f16e2dd9fe-20260609T223759520787+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/fc4580a78627

## What looked useful

N-gram self-drafting on CPU is cheap, but simple n-gram/prompt-lookup drafts only appear useful for repeated local spans or template-like text. On a natural-text held-out stream, accepted draft length was too low to support a paper claim.

## Boundaries and scale limits

No real transformer model was benchmarked because the local environment lacks torch/transformers. The target model was proxied by held-out token streams, so results measure draft-token matchability and CPU lookup overhead rather than end-to-end model wall-clock speed.

## Claim scope

Bounded CPU proxy benchmark of static train n-gram and dynamic prompt-lookup draft tokens against held-out token streams. The mechanism gives large ideal verifier-call reductions on highly repetitive synthetic streams but only 1.104x best-case ideal call reduction on Tiny Shakespeare natural text, before real transformer verification overhead.

## Why it stopped

Bounded proxy evidence did not meet the natural-text success threshold: best Tiny Shakespeare ideal verifier-call speedup was 1.104x, and actual transformer wall-clock speedup would likely be lower after verification overhead.

## Recommended next action

Stop this run as a no-paper useful signal; a bounded follow-up should run a real CPU GPT-2-small-class greedy baseline versus dynamic prompt-lookup speculative decoding on separated repetitive and open-ended prompt sets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU LM benchmark for dynamic prompt-lookup speculative decoding
- Success threshold: At least 1.25x wall-clock speedup on a natural/open-ended prompt set, or greater than 1.5x on a clearly scoped repetitive/template-heavy CPU workload with unchanged greedy outputs.
- Stop condition: Stop if real-model wall-clock speedup is below 1.1x on both prompt classes or if verification overhead removes the call-count benefit.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-decoding-with-n-gram-draft-tokens-on-cpu-47f16e2dd9fe`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
