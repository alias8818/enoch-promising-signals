# Layer-skip self-speculative decoding on GB10

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `68`
Project ID: `layer-skip-self-speculative-decoding-on-gb10-ef0f9c4d49d9`
Run ID: `layer-skip-self-speculative-decoding-on-gb10-ef0f9c4d49d9-20260612T034129077685+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `68`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/13353fe01b83

## What looked useful

GB10 comfortably ran a 1B LayerSkip-style model in BF16 and the native assistant_early_exit path executed, but exit layers 4/8/12 measured 0.83x/0.72x/0.66x baseline throughput and reproduced exact greedy output for only 3 of 6 prompts.

## Boundaries and scale limits

Short local inference benchmark only: 1B accessible derivative checkpoint, six prompts, 48 new tokens each, greedy decoding, no task dataset, no official facebook/layerskip-llama3.2-1B access because the repo returned HTTP 403 gated access, no larger 7B+ validation.

## Claim scope

On this GB10 worker, native Transformers self-speculative decoding with assistant_early_exit on the accessible melhoushi/layerskip-llama3.2-1b-topv1-v5 checkpoint was slower than ordinary greedy decoding across six short prompts and only matched baseline greedy token sequences on half of prompts.

## Why it stopped

Bounded negative/useful-signal result: the accessible checkpoint did not accelerate generation on GB10 and did not consistently preserve baseline greedy token sequences; the official small checkpoint was gated from this worker.

## Recommended next action

Stop as no-paper local evidence; rerun only if authorized access to an official LayerSkip checkpoint is available, with exact-equivalence checks and a broader prompt/task benchmark.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/layer-skip-self-speculative-decoding-on-gb10-ef0f9c4d49d9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
