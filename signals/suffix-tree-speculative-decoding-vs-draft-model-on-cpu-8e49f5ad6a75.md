# Suffix-Tree Speculative Decoding vs Draft-Model on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-speculative-decoding-vs-draft-model-on-cpu-8e49f5ad6a75`
Run ID: `suffix-tree-speculative-decoding-vs-draft-model-on-cpu-8e49f5ad6a75-20260629T190305305259+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/0b7c62679c96

## What looked useful

Suffix indexing has a plausible niche for long-context repetition, reaching 1.144x the n-gram draft proxy's tokens per verifier call on the targeted corpus, but it lost on boilerplate and tied on low-repetition streams while carrying higher prototype overhead.

## Boundaries and scale limits

No real LLM verifier or trained neural draft model was run; tokenizer, KV-cache, batched verifier latency, and compiled suffix-index overhead remain untested.

## Claim scope

Offline CPU decoding-trace proxy with deterministic token corpora: suffix-index speculation only improved verifier-call reduction on a targeted long-context repeated-continuation workload, not across broader synthetic boilerplate, Markov, or random streams.

## Why it stopped

Bounded proxy evidence is mixed and does not support a broad paper claim; it identifies only a narrow workload niche.

## Recommended next action

Stop this run as no-paper evidence; if deepening, run a bounded real small-LLM CPU benchmark on natural repeated-context corpora with a compiled suffix proposer and trained draft-model baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real small-LLM CPU benchmark for suffix-index speculation on repeated-context corpora
- Success threshold: At least 1.15x wall-clock tokens/s over the trained draft-model baseline on high-repetition natural corpora, with no regression below 0.95x on ordinary boilerplate workloads.
- Stop condition: Stop if suffix-index wall-clock speed is below the trained draft-model baseline on high-repetition corpora or if proposer overhead consumes more than 25% of decode time.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-speculative-decoding-vs-draft-model-on-cpu-8e49f5ad6a75`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
