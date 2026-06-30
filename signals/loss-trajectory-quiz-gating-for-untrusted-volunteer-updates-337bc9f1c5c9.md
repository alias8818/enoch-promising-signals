# Loss-Trajectory Quiz Gating for Untrusted Volunteer Updates

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `loss-trajectory-quiz-gating-for-untrusted-volunteer-updates-337bc9f1c5c9`
Run ID: `loss-trajectory-quiz-gating-for-untrusted-volunteer-updates-337bc9f1c5c9-20260613T033322066474+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/908164cba090

## What looked useful

Loss-trajectory quizzes improved final accuracy versus random quizzes from 0.895969 to 0.968255 and accepted more helpful updates, but accepted more poison than targeted quizzes and finished below targeted quiz accuracy.

## Boundaries and scale limits

Synthetic proxy only: no real volunteer data, no natural-language update parsing, no learned model training, no adaptive adversaries, and no production operator workflow.

## Claim scope

In a deterministic synthetic per-region threshold-update simulation over 80 seeds, loss-trajectory quiz gating outperformed accept-all, static reputation, and random quiz gating on final accuracy, but was dominated by a simpler targeted quiz gate.

## Why it stopped

Bounded synthetic evidence is mixed: useful versus weak baselines but insufficient and partly negative versus the strongest simple baseline.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should combine targeted update-scope quiz items with loss-trajectory item weighting and compare against targeted-only gating.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hybrid Targeted and Loss-Trajectory Quiz Gating
- Success threshold: Hybrid final accuracy within 0.003 of targeted_quiz_gate while poison_accept_rate stays at or below 0.02 and helpful_accept_rate is at least 0.38 over 80 matched seeds.
- Stop condition: Stop if hybrid poison_accept_rate exceeds 0.04 or final accuracy is more than 0.01 below targeted_quiz_gate after the matched 80-seed run.

## Evidence references

- Artifact root: `<local-path>/projects/loss-trajectory-quiz-gating-for-untrusted-volunteer-updates-337bc9f1c5c9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
