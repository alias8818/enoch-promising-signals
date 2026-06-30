# Agent Memory Architecture: Doctrine vs Fact Retention

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `agent-memory-architecture-doctrine-vs-fact-retention-bb91fb635f35`
Run ID: `agent-memory-architecture-doctrine-vs-fact-retention-bb91fb635f35-20260628T212842054822+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/34fc6b6ab6e3

## What looked useful

Doctrine retention showed large gains in stable structured settings, near-zero or negative gains in no-doctrine entity-random settings, and worse post-drift accuracy than fact retention. This suggests doctrine memory needs drift handling and should be used conditionally rather than as a universal replacement for fact retention.

## Boundaries and scale limits

Toy synthetic stream only; no LLM, no learned natural-language doctrine extraction, no real conversation memory, no embedding retrieval, no explicit token/compute cost for extracting doctrine. Runs used 4 scenarios, 4 budgets, 3 policies, 10 seeds, and 2000 steps per trial.

## Claim scope

In a deterministic synthetic bounded-memory stream benchmark, doctrine/rule retention outperforms fact-only retention when stable group-level regularities exist and queries include unseen entities, but it is neutral to worse when actions are entity-specific and brittle after rule drift.

## Why it stopped

No-paper closure: evidence is a synthetic mechanism signal, not direct publication-grade validation of real agent memory architecture.

## Recommended next action

Run a bounded deepen follow-up that adds adaptive doctrine decay/versioning and evaluates it against fact-only and hybrid controls on the same drift benchmark plus a small natural-language memory task.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive doctrine retention with drift detection for bounded agent memory
- Success threshold: Adaptive doctrine matches or exceeds naive doctrine on stable structured accuracy and improves post-drift accuracy by at least 0.15 absolute over naive doctrine without falling below fact-only post-drift accuracy.
- Stop condition: Stop if adaptive doctrine cannot beat naive doctrine post-drift by 0.10 absolute in the synthetic drift setting, because the main failure mode from this run remains unresolved.

## Evidence references

- Artifact root: `<local-path>/projects/agent-memory-architecture-doctrine-vs-fact-retention-bb91fb635f35`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
