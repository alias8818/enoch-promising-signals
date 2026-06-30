# Agent Memory Architecture: Does Semantic Compression Build Operator Doctrine?

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `agent-memory-architecture-does-semantic-compression-build-operator-doctrine-d8b8c98668c8`
Run ID: `agent-memory-architecture-does-semantic-compression-build-operator-doctrine-d8b8c98668c8-20260613T063735232858+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/62aab312ff43

## What looked useful

Semantic compression reached 0.8136 mean accuracy versus 0.7286 for raw episodic kNN and 0.3331 for majority baseline, while using about 1.97% of the raw episodic footprint and recovering 65.75% mean hidden-rule recall at the rule budget. Noise sweeps at 0%, 8%, and 20% training-label noise kept semantic compression 6.6 to 9.5 accuracy points ahead of episodic retrieval.

## Boundaries and scale limits

Synthetic one-step classification only; no real agent traces, no LLM summarizer, no embedding retrieval baseline, no long-horizon tool use, and no production memory store. Full run used 80 seeds with 360 train and 720 test episodes per seed, completing in about 26 seconds on one CPU core.

## Claim scope

In a synthetic rule-governed incident-response benchmark, deterministic semantic compression of episodes into compact feature-action rules improves held-out action selection over raw token-overlap episodic kNN and recovers a measurable subset of the hidden operator doctrine.

## Why it stopped

No-paper closure: positive synthetic mechanism signal, but broader agent-memory/operator-doctrine claim remains proxy-only and lacks strong retrieval controls or real operational traces.

## Recommended next action

Run a bounded deepen follow-up comparing LLM-style semantic summaries and embedding retrieval baselines on semi-real operational traces before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Embedding and LLM-summary controls for semantic doctrine memory
- Success threshold: Semantic/LLM-compressed doctrine beats raw embedding episodic retrieval by at least 5 absolute accuracy points on held-out traces while using no more than 25% of the raw memory footprint and without worse distribution-shift performance.
- Stop condition: Stop if semantic compression fails to beat raw embedding retrieval by 2 absolute accuracy points in a smoke run of at least 200 held-out decisions, or if doctrine summaries cannot be evaluated against trace labels without human/private evidence.

## Evidence references

- Artifact root: `<local-path>/projects/agent-memory-architecture-does-semantic-compression-build-operator-doctrine-d8b8c98668c8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
