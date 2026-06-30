# CPU-side Bounded N-gram Trie Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-side-bounded-n-gram-trie-speculative-decoding-0bbad629149d`
Run ID: `cpu-side-bounded-n-gram-trie-speculative-decoding-0bbad629149d-20260629T203541563554+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/66ef8919d7d2

## What looked useful

The mechanism is useful when future tokens repeat from prior context and essentially inactive on high-entropy random traces, so it is a workload-conditional acceleration idea rather than a general decoding speedup.

## Boundaries and scale limits

Proxy-only experiment: no real transformer target, no model tokenizer IDs, no production implementation, no batching/server integration, and project_text was repeated from a small scaffold corpus.

## Claim scope

A Python CPU-side bounded n-gram trie reduced target verification calls under an exact-match trace proxy on repeated-context workloads, reaching 6.99 emitted tokens per target call on synthetic repeated traces at gamma=8 and max_order=4, while iid-random traces stayed near 1.00.

## Why it stopped

Closed as no-paper useful signal because the current evidence is a trace proxy, not end-to-end LLM serving validation.

## Recommended next action

Run a bounded direct-evidence follow-up on real model-token traces and compare against prompt-lookup decoding, no-spec decoding, and a small draft-model speculative baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-token bounded n-gram trie speculative decoding comparison
- Success threshold: At least 1.3x end-to-end latency improvement or target-call reduction on repeated-context traces with less than 5% regression on low-repeat traces under a fixed memory cap.
- Stop condition: Stop if repeated-context real-token traces fail to exceed 1.1 emitted tokens per target call or CPU trie overhead erases target-call savings.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-side-bounded-n-gram-trie-speculative-decoding-0bbad629149d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
