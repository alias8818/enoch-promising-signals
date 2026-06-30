# N-gram Speculative Drafting on CPU Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-speculative-drafting-on-cpu-inference-5f916d866a43`
Run ID: `n-gram-speculative-drafting-on-cpu-inference-5f916d866a43-20260527T071843101906+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/ca553ab2b4b6

## What looked useful

On LLM-like word tokens, best optimistic speedup was only 1.107x with 9.6% target-call reduction, 1.8% draft-token acceptance, about 0.14 accepted tokens per draft attempt, and 0% full-block acceptance at gamma 8. A repetitive synthetic control reached about 7.4x optimistic speedup and 96% draft-token acceptance, showing n-gram drafting can help only when continuation copying is common.

## Boundaries and scale limits

No end-to-end transformer CPU inference was run. The target model was proxied by held-out trace replay, and speedup is optimistic target-call accounting rather than measured model tokens/s. Natural text coverage is limited to Tiny Shakespeare with 24 offsets and 512 generated tokens per trial.

## Claim scope

Bounded replay benchmark of n-gram speculative drafting on Tiny Shakespeare word/byte token traces plus a synthetic repeated-stanza control. Evidence supports the mechanism for highly repetitive continuations but not a broad general CPU-inference speedup claim.

## Why it stopped

Proxy replay early-falsified the broad/general natural-text hypothesis while preserving a special-case repetitive-workload mechanism; this is not a full end-to-end validation.

## Recommended next action

Stop this run as no-paper useful signal; a bounded follow-up should run the same drafter inside a real CPU transformer or llama.cpp-style verifier on repetitive-template workloads and general prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end CPU n-gram speculative verification on repetitive workloads
- Success threshold: At least 1.25x measured tokens/s on repetitive workloads with no more than 3% regression on general prompts, over at least 100 prompts or an equivalent fixed-token benchmark.
- Stop condition: Stop if best measured end-to-end speedup remains below 1.10x on repetitive workloads or if general-prompt regression exceeds 10% after tuning gamma/max n.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-drafting-on-cpu-inference-5f916d866a43`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
