# Persistent Suffix-Trie Draft Store for Cross-Session Spec

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `persistent-suffix-trie-draft-store-for-cross-session-spec-40261003a63e`
Run ID: `persistent-suffix-trie-draft-store-for-cross-session-spec-40261003a63e-20260620T163141369196+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c76634a5b68a

## What looked useful

Persistent suffix-trie indexing is a useful retrieval component for substring/suffix phrasing, but the tested primary-store design is insufficient for current structured state because suffix-only matches often retrieve the right field from the wrong spec. A canonical snapshot/current-state layer dominated it for this task.

## Boundaries and scale limits

10 seeds, 24 specs, 24 sessions, 3,840 deterministic field-recovery queries; synthetic data only, deterministic extraction only, no real operator corpus, no LLM agent loop, no concurrency or crash-recovery validation.

## Claim scope

On a seeded synthetic cross-session spec-field recovery benchmark, a persistent suffix-trie memory index preserved answers across reloads, achieved 1.0000 direct-query accuracy, and improved suffix-anchored accuracy over transcript and flat retrieval baselines, but it did not match a simple snapshot dictionary control.

## Why it stopped

No-paper closure: bounded local evidence is mixed and shows the current suffix-trie primary-store design is dominated by a snapshot dictionary control for structured current-state recovery.

## Recommended next action

Run a bounded deepen experiment with spec-aware recency/current-state routing layered on the suffix trie, and require snapshot-level direct accuracy plus materially better suffix-anchored retrieval than flat retrieval.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Spec-aware suffix-trie retrieval with current-state routing
- Success threshold: Direct accuracy must equal snapshot_dict at 1.0000 and suffix-anchored accuracy must be at least 0.90 across 10 seeds without more than 2x the current suffix-trie query latency.
- Stop condition: Stop if direct accuracy falls below 1.0000, suffix-anchored accuracy remains below 0.80, persistence reload checks fail, or memory/index size grows by more than 3x without accuracy gains.

## Evidence references

- Artifact root: `<local-path>/projects/persistent-suffix-trie-draft-store-for-cross-session-spec-40261003a63e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
