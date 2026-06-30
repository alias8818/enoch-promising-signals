# Memory Architecture: Operator Doctrine Distillation

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `memory-architecture-operator-doctrine-distillation-ce29b48301e5`
Run ID: `memory-architecture-operator-doctrine-distillation-ce29b48301e5-20260613T104901972542+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/274266e08693

## What looked useful

Rule-modality extraction alone over-prioritized some late resource/follow-up rules and dropped important decision-gating rules; preserving prompt position or section semantics appears necessary before operator-doctrine distillation is worth scaling.

## Boundaries and scale limits

Single corpus, eight hand-coded probes, lexical retrieval and judging, no learned extractor, no deployed agent memory system, and no multi-corpus robustness test.

## Claim scope

On the Enoch controller prompt corpus and eight explicit operational-rule probes, a simple lexical operator-doctrine distiller did not improve compact-memory rule retrieval over first-N truncation at 80-500 word budgets.

## Why it stopped

Proxy/local evaluation falsified the simple operator-doctrine heuristic: it never beat first-N truncation and lost at one tested budget, so this is not paper-ready full validation.

## Recommended next action

Stop this run as a proxy negative result; run one bounded deepen follow-up with a position-aware operator distiller over at least three controller/operator corpora.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Position-Aware Operator Doctrine Distillation
- Success threshold: Position-aware operator doctrine memory improves mean rule-retrieval accuracy by at least 20 percentage points over first-N at two or more matched budgets without losing any critical decision-gate probes.
- Stop condition: Stop if the method fails to beat first-N on at least two of three corpora or if gains disappear when query terms are withheld from extraction.

## Evidence references

- Artifact root: `<local-path>/projects/memory-architecture-operator-doctrine-distillation-ce29b48301e5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
