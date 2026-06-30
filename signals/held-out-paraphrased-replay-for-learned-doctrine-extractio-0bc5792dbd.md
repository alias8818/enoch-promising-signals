# Held-out paraphrased replay for learned doctrine extraction

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `held-out-paraphrased-replay-for-learned-doctrine-extractio-0bc5792dbd`
Run ID: `held-out-paraphrased-replay-for-learned-doctrine-extractio-0bc5792dbd-20260613T082719120189+0000`

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

- Parent run decision: Memory-Architecture Agent with Learned Operator Doctrine: enoch://control-plane/projects/memory-architecture-agent-with-learned-operator-doctrine-45b2224071c2/runs/memory-architecture-agent-with-learned-operator-doctrine-45b2224071c2-20260613T072931308109+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/e553faf733bb

## What looked useful

Corrected Tier 1 direct test met the predefined threshold: layered_doctrine_memory reached 24/24 accuracy (1.000) versus best baseline 6/24 (0.250), margin 0.750.

## Boundaries and scale limits

Synthetic corpus; fixed concept lexicon; small action set; no open-ended agent behavior; no human-authored paraphrases; no large model or real transcript extraction.

## Claim scope

In a deterministic synthetic replay classification task with 8 doctrines, 24 training cases, and 24 held-out paraphrased cases, a concept-level doctrine memory strategy preserved doctrine actions across paraphrases better than majority, transcript-search, and flat TF-IDF retrieval baselines.

## Why it stopped

No-paper closure: the mechanism is supported in a small controlled synthetic direct test, but evidence is lexicon-assisted and not broad or natural enough for publication readiness.

## Recommended next action

Run a bounded deepen follow-up that removes the fixed concept lexicon and learns doctrine mappings from noisy replay text, then evaluates on independently authored paraphrases.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned doctrine induction without fixed cue lexicon on noisy paraphrased replays
- Success threshold: Extractor-based doctrine memory accuracy >= 0.80, at least 0.20 absolute margin over best baseline, and no detected train/test lexical leakage in distractors or labels.
- Stop condition: Stop as negative if extractor accuracy is below 0.65 or margin over best baseline is below 0.10 after leakage checks on the bounded corpus.

## Evidence references

- Artifact root: `<local-path>/projects/held-out-paraphrased-replay-for-learned-doctrine-extractio-0bc5792dbd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
