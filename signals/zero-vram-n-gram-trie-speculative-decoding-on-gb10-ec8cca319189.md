# Zero-VRAM N-Gram Trie Speculative Decoding on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `zero-vram-n-gram-trie-speculative-decoding-on-gb10-ec8cca319189`
Run ID: `zero-vram-n-gram-trie-speculative-decoding-on-gb10-ec8cca319189-20260621T002822222583+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ae38755bc9f2

## What looked useful

The mechanism is viable when continuations overlap prompt context: copy-heavy cases reached 1.0 acceptance and 0.82 forward-count reduction, while open-ended cases reached only 0.083 acceptance and nearly no forward-count reduction. A 32k-token synthetic CPU trie built in 0.22 s, used about 39 MB RSS, and served lookups at about 1.65 us each including Python context slicing.

## Boundaries and scale limits

Small synthetic prompts, distilgpt2 target model, full-context use_cache=False verifier, no production KV-cache serving path, no real RAG/summarization dataset, no large external datastore, and no 7B+ model validation.

## Claim scope

On a GB10 worker with cached distilgpt2, a CPU-resident n-gram trie drafter preserved exact greedy outputs and provided high acceptance on small copy-heavy prompt-overlap cases, but not on open-ended prompts. Trie lookup overhead was microsecond-scale in the Python probe.

## Why it stopped

Proxy local evidence supports the copy-overlap mechanism but is insufficient and not novel enough for a paper; open-ended prompt-only acceptance is poor and timing uses a non-production full-context verifier.

## Recommended next action

Stop this run as a no-paper useful signal; the concrete next bounded action is a KV-cache-preserving verifier benchmark on cached 0.5B-3B models with real copy-heavy RAG prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache n-gram trie verifier on real copy-heavy RAG prompts
- Success threshold: At least 1.2x median wall-clock speedup over KV-cache greedy decoding on copy-heavy prompts with exact output preservation, less than 5% slowdown on open-ended controls, and documented CPU memory overhead.
- Stop condition: Stop if acceptance remains below 0.25 on copy-heavy prompts, exact outputs diverge, or KV-cache verifier overhead erases speedup versus greedy baseline.

## Evidence references

- Artifact root: `<local-path>/projects/zero-vram-n-gram-trie-speculative-decoding-on-gb10-ec8cca319189`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
